import json
import mimetypes
import os
import shutil
import subprocess
import time
from itertools import product

import fiona
import geopandas as gpd
import pandas as pd
import rasterio as rio
import requests
from geo.Geoserver import Geoserver, GeoserverException
from rasterio.enums import ColorInterp
from rasterio.features import rasterize
from rasterio.windows import Window

from . import ortho, storage

GEOSERVER_URL = os.environ.get(
    "GEOSERVER_URL", r"https://geonode.seabee.sigma2.no/geoserver"
)
GEONODE_URL = os.environ.get("GEONODE_URL", r"https://geonode.seabee.sigma2.no/api/v2/")
DEFAULT_BAND_ORDER = ["nir", "rededge", "red", "green", "blue"]
COLOUR_INTERP_DICT = {
    "red": ColorInterp.red,
    "green": ColorInterp.green,
    "blue": ColorInterp.blue,
    "nir": ColorInterp.undefined,
    "rededge": ColorInterp.undefined,
    "lwir": ColorInterp.undefined,
    "panchro": ColorInterp.gray,
    "alpha": ColorInterp.alpha,
}
DEFAULT_LICENCE = "CC-BY-4"
DEFAULT_LICENCE_LINK = "https://creativecommons.org/licenses/by/4.0/"


def get_geotiff_info(tif_path):
    """Read basic metadata from a GeoTiff.

    Args
        tif_path: Str. Path to GeoTiff.

    Returns
        Dict of properties. E.g.:
            {
                "file_name": fname,
                "mission_name": mission_name,
                "mission_dir": mission_dir,
                "num_bands": nbands,
                "pixel_dtype": dtype,
                "band_descriptions": {"red": 1, "green": 2, "blue": 3},
                "crs": "epsg:25833",
                "nodata_value": None,
            }

    Raises
        ValueError if the GeoTiff has multiple NoData values.
    """
    # Get basic file path info
    fname = os.path.basename(tif_path)
    mission_dir = os.path.dirname(os.path.dirname(tif_path))
    mission_name = os.path.basename(mission_dir)

    # Read properties from file
    with rio.open(tif_path) as src:
        nbands = src.count
        band_descriptions = _get_band_info(src)
        if len(band_descriptions) == nbands:
            # We can uniquely identify each band
            band_info = band_descriptions
        else:
            # Can't identify with confidence; set to None
            band_info = None

        info_dict = {
            "file_name": fname,
            "mission_name": mission_name,
            "mission_dir": mission_dir,
            "num_bands": nbands,
            "pixel_dtype": src.dtypes[0],
            "band_descriptions": band_info,
            "crs": str(src.crs),
        }

        nodata_values = set(nodata for nodata in src.nodatavals)
        if len(nodata_values) == 1:
            info_dict["nodata_value"] = nodata_values.pop()
        else:
            raise ValueError(
                f"'{tif_path}' has multiple NoData values: {nodata_values}."
            )

    return info_dict


def _get_band_info(src):
    """Merge band information contained in 'band_descriptions' and 'colorinterp'
    into a single dict.

    Args
        src: Obj. Open rasterio dataset.

    Returns
        Dict of band information 'description' => 'band_num'.
    """
    band_info = {
        idx + 1: (desc.lower() if desc else None)
        or (colour.name.lower() if colour.name else None)
        for idx, (desc, colour) in enumerate(zip(src.descriptions, src.colorinterp))
    }
    merged = {info: band for band, info in band_info.items() if info is not None}

    return merged


def _rename_key(d, old_key, new_key):
    """Rename a key in a dict inplace.

    Args
        d: Dict to be modified.
        old_key: Hashable. Old key to be replaced.
        new_key: Hashable. New key.

    Returns
        Dict. 'd' is modified inplace.
    """
    if old_key in d:
        d[new_key] = d.pop(old_key)
    return d


def infer_geotiff_metadata(tif_path):
    """If accurate metadata cannot be read directly from a GeoTIFF, this function
    attempts to "guess" based on other dataset properties.

    Args
        tif_path: Str. Path to GeoTiff.

    Returns
        Dict of GeoTiff properties.

    Raises
        ValueError if the band order cannot be inferred from the number of bands.
    """
    # Read metadata from the file if possible
    info_dict = get_geotiff_info(tif_path)

    # Infer bands if not explicitly provided
    band_dict = info_dict.get("band_descriptions")
    if band_dict is None:
        # Get other data to help with guessing
        spec = (
            ortho.parse_config(info_dict["mission_dir"])
            .get("spectrum_type", "rgb")
            .lower()
        )  # Assume RGB if not specified
        nbands = info_dict["num_bands"]

        # Heuristics for guessing band order
        if nbands == 3:
            # Assume RGB
            info_dict["band_descriptions"] = {"red": 1, "green": 2, "blue": 3}
        elif (nbands == 4) and (spec == "rgb"):
            # Assume RGBA
            info_dict["band_descriptions"] = {
                "red": 1,
                "green": 2,
                "blue": 3,
                "alpha": 4,
            }
        elif (nbands == 5) and (spec == "msi"):
            # Assume MS dataset created manually in correct order i.e.
            # NIR, RedEdge, Red, Green, Blue
            info_dict["band_descriptions"] = {
                "nir": 1,
                "rededge": 2,
                "red": 3,
                "green": 4,
                "blue": 5,
            }
        else:
            raise ValueError(f"Could not determine band order for '{tif_path}'.")

    # Standardise 're' to 'rededge'
    _rename_key(info_dict["band_descriptions"], "re", "rededge")

    return info_dict


def restructure_orthophoto(
    in_tif,
    out_tif,
    band_dict,
    band_order=["nir", "rededge", "red", "green", "blue"],
    nodata=0,
):
    """Create a standardised, cloud-optimised GeoTIFF from an orthophoto. Bands
    are re-ordered to match 'band_order' and converted to 8-bit (with value
    scaling). Any alpha bands are removed and pixel values equal to 'nodata' are
    set as NoData. Existing overview layers are discarded and rebuilt. The file
    is saved using LZW compression.

    Args
        in_tif:     Str. Path to original GeoTIFF.
        out_tif:    Str. Path to GeoTIFF to be created. Must be in a folder where
                    you have "write" access i.e. somewhere in your HOME directory.
        band_dict:  Dict mapping lowercase band names ('nir', 'rededge' etc.) to band
                    numbers in 'in_tif'.
        band_order: List. Default ["nir", "rededge", "red", "green", "blue"]. List
                    specifiying the band order (1 to n) to create in 'out_tif'. If
                    a band name in 'band_order' is not found in 'band_dict', it
                    will be skipped. E.g. if 'in_tif' is an RGBA raster, you can
                    still use the default 'band_order' and 'nir' and 'rededge' will be
                    ignored, creating an 'out_tif' with R, G, B as bands 1, 2, 3.
        nodata:     Int between 0 and 255. Default 0. Value to consider as NoData.
                    Note that this function does not change an existing NoData value
                    to a new value, it simply sets the NoData value in 'out_tif' to
                    the value specified.

    Returns
        None. Raster is saved to the specified path.

    Raises
        ValueError if 'nodata' is not an integer.
        ValueError if 'nodata' is not between 0 and 255.
        ValueError if 'band_order' contains elements not in 'red', 'green', 'blue',
            'rededge', 'nir'.
    """
    if not isinstance(nodata, int):
        raise ValueError("'nodata' must be an integer.")
    if not (0 <= nodata <= 255):
        raise ValueError("'nodata' must be between 0 and 255.")
    if not set(band_order).issubset(set(["nir", "rededge", "red", "green", "blue"])):
        raise ValueError(
            f"Currently supported bands are ['nir', 'rededge', 'red', 'green', 'blue'], not {band_order}."
        )

    # Make a copy of the original file for editing
    temp_tif = os.path.join(os.path.dirname(out_tif), "temp2.tif")
    shutil.copyfile(in_tif, temp_tif)

    # Explictly set inferred band metadata on the copy
    desc_dict = {val: key for key, val in band_dict.items()}
    with rio.open(temp_tif, "r+") as ds:
        nbands = ds.count
        for bidx in range(nbands):
            ds.set_band_description(bidx + 1, desc_dict.get(bidx + 1, "none"))
        colorinterps = [
            COLOUR_INTERP_DICT.get(desc_dict.get(idx + 1), ColorInterp.undefined)
            for idx in range(nbands)
        ]
        ds.colorinterp = tuple(colorinterps)

    # Build command for GDAL
    cmd = [
        "gdal_translate",
        "-of",
        "COG",
        "-ot",
        "Byte",
        "-co",
        "COMPRESS=LZW",
        "-co",
        "PREDICTOR=2",
        "-co",
        "NUM_THREADS=4",
        "-co",
        "OVERVIEWS=IGNORE_EXISTING",
        "-co",
        "BIGTIFF=YES",
        "-scale",
        "-a_nodata",
        str(nodata),
        temp_tif,
        out_tif,
    ]
    for band in band_order[::-1]:
        if band in band_dict:
            cmd.insert(1, str(band_dict[band]))
            cmd.insert(1, "-b")

    subprocess.check_call(cmd)

    # Delete the temporary file
    os.remove(temp_tif)


def adjust_nodata(
    in_tif,
    out_tif,
    orig_nodata,
    band_dict,
    new_nodata=0,
    reclass_value=1,
    alpha_band_nodata=0,
):
    """Sets the NoData value in a raster based on the alpha band.

    By default, ODM and Pix4D use an alpha mask to define NoData in output
    orthomosaics. For the ML algorithms, NR would prefer an explicit NoData value
    (see https://github.com/SeaBee-no/documentation/issues/30).

    This function explicitly sets a user-specified NoData value where values in
    the alpha mask are equal to 'alpha_band_nodata'. Before updating values based
    on the mask, any valid values equal to the new NoData value are first
    relcassified to 'reclass_value'.

    For example, by default ODM produces 8-bit RGB images where valid band values
    range from 0 to 255 and values of 0 in the alpha channel represent NoData.
    Using the default arguments, this function will first change valid band values
    of 0 to 1 (which should not affect the ML - see issue above), and then set
    band values to zero where the alpha mask is zero.

    NOTE: This function assumes that the alpha band is always the last band in the
    mosaic.

    Args
        in_tif:            Str. Path to input GeoTIFF file.
        out_tif:           Str. Path to GeoTIFF to be created. Must be in a folder
                           where you have "write" access i.e. somewhere in your
                           HOME directory.
        orig_nodata:       Int, Float or None. NoData value defined for 'in_tif'.
        band_dict:         Dict mapping lowercase band names ('nir', 'rededge' etc.)
                           to band numbers in 'in_tif'.
        new_nodata:        Int. Default 0. Value to set as 'nodata' in 'out_tif'.
        reclass_value:     Int. Default 1. Value to assign to valid data that is
                           equal to 'new_nodata'.
        alpha_band_nodata: Int. Default 0. Value in the alpha band that indicates
                           NoData.

    Returns
        None. Raster is saved to the specified path.

    Raises
        ValueError if 'nodata_value', 'reclass_value', or 'alpha_band_nodata' are
            not integers.
        ValueError if 'nodata_value', 'reclass_value', or 'alpha_band_nodata' are
            not between 0 and 255.
    """
    variables = {
        "new_nodata": new_nodata,
        "reclass_value": reclass_value,
    }
    for var_name, val in variables.items():
        if not isinstance(val, int):
            raise ValueError(f"'{var_name}' must be an integer.")
        if not (0 <= val <= 255):
            raise ValueError(f"'{var_name}' must be between 0 and 255.")

    with rio.open(in_tif) as src:
        profile = src.profile
        profile.update(compress="LZW", BIGTIFF="YES")

        with rio.open(out_tif, "w", **profile) as dst:
            for ji, window in src.block_windows(1):
                data = src.read(window=window)

                if "alpha" in band_dict:
                    alpha_idx = band_dict["alpha"] - 1
                    if orig_nodata is None:
                        # Metadata are specificed correctly using alpha channel. Applies to
                        # all ODM missions (both RGB and MSI), and some Pix4D RGB missions.
                        # Use alpha == alpha_band_nodata to represent NoData
                        alpha_mask = data[alpha_idx] == alpha_band_nodata
                        for bidx in range(data.shape[0]):
                            if bidx != alpha_idx:
                                # Set valid values that are equal to 'new_nodata' to the
                                # 'reclass_value'
                                data[bidx][data[bidx] == new_nodata] = reclass_value

                                # Set band values to 'new_nodata' where the alpha band is
                                # equal to 'alpha_band_nodata'
                                data[bidx][alpha_mask] = new_nodata
                    else:
                        # Alpha and an explicit NoData value are specified. Assume alpha
                        # represents something else and use the explicit NoData value
                        for bidx in range(data.shape[0]):
                            if (bidx != alpha_idx) and (new_nodata != orig_nodata):
                                data[bidx][data[bidx] == new_nodata] = reclass_value
                                data[bidx][data[bidx] == orig_nodata] = new_nodata
                else:
                    # No alpha channel
                    if orig_nodata is None:
                        # NoData info missing completely. Applies to many Pix4D MSI missions
                        # where the alpha channel has been discarded, but no new NoData
                        # value assigned. Assume orig_nodata is zero.
                        orig_nodata = 0

                    # The NoData value is specified explicitly. Applies to some Pix4D missions.
                    if new_nodata != orig_nodata:
                        data[data == new_nodata] = reclass_value
                        data[data == orig_nodata] = new_nodata

                dst.write(data, window=window)

            dst.descriptions = src.descriptions
            dst.colorinterp = src.colorinterp


def standardise_orthophoto(in_tif, out_tif):
    """Create a SeaBee standard orthophoto.

    Args
        in_tif:            Str. Path to input GeoTIFF file.
        out_tif:           Str. Path to GeoTIFF to be created. Must be in a folder
                           where you have "write" access i.e. somewhere in your
                           HOME directory.

    Returns
        None. 'out_tif' is created.
    """
    # Infer metadata from GeoTiff
    info_dict = infer_geotiff_metadata(in_tif)
    band_dict = info_dict["band_descriptions"]
    orig_nodata = info_dict["nodata_value"]

    # Standardise NoData
    temp_fold = os.path.split(out_tif)[0]
    temp_tif = os.path.join(temp_fold, "temp.tif")
    adjust_nodata(
        in_tif,
        temp_tif,
        orig_nodata,
        band_dict,
        new_nodata=0,
        reclass_value=1,
        alpha_band_nodata=0,
    )

    # Restructure
    restructure_orthophoto(
        temp_tif,
        out_tif,
        band_dict,
        band_order=DEFAULT_BAND_ORDER,
        nodata=0,
    )
    os.remove(temp_tif)


def upload_geopackage_to_geoserver(
    fpath: str, user: str, password: str, workspace="geonode"
) -> str:
    """Upload a geopackage from JupyterHub to GeoServer. The name of the geopackage
    will be used as a datastore and the first layer in the geopackage published as
    a layer.

    Only the first layer in the geopackage will be published. If you need
    more control over exactly which layers are published, use
    'upload_geopackage_layers_to_geoserver' instead.

    NOTE: Creation of the layer will be overwritten if it exist

    Args
        fpath:     Str. Path to geopackage dataset to be uploaded
        user:      Str. GeoServer admin. user
        password:  Str. GeoServer admin. password
        workspace: Str. Default 'geonode'. GeoServer workspace

    Returns
        Str.
    """

    headers = {
        "Content-type": "application/x-sqlite3",
    }

    store_name = os.path.splitext(os.path.basename(fpath))[0]

    url = (
        f"{GEOSERVER_URL}/rest/workspaces/{workspace}/datastores/{store_name}/file.gpkg"
    )

    with open(fpath, "rb") as f:
        r = requests.put(
            url,
            data=f.read(),
            auth=(user, password),
            headers=headers,
        )
    if r.status_code in [200, 201, 202]:
        return store_name
    else:
        raise GeoserverException(r.status_code, r.content)


def upload_geopackage_layers_to_geoserver(
    gpkg_path,
    layers,
    username,
    password,
    workspace="geonode",
    style_dict=None,
):
    """Upload a list of layers from a geopackage to GeoServer, including optional
    styling. Provides more control than 'upload_geopackage_to_geoserver', which
    only uploads the first layer.

    Args
        gpkg_path: Str. Path to geopackage.
        layers: List of str. List of layer names to publish.
        username: Str. Admin. username for GeoServer.
        password: Str. Admin. password for GeoServer.
        workspace: Str. Default 'geonode'. Workspace to upload to.
        style_dict: Dict. Optional. Default None. Dict mapping layer names to SLD
            files for styling layers. Dict values can either be paths to local .sld
            files or the names of standard SeaBee SLD files hosted on GitHub here:
                https://github.com/SeaBee-no/annotation/tree/main/sld_files
            Example dict values:
                '/path/to/local/file.sld' (local file)
                'annotation_classes_v{version}_level{level}.sld' (hosted on GitHub)
            In both cases, the .sld extension should be included.

    Returns
        Str. The name of the data store created (the same as the geopackage name
        but without the .gpkg extension).
    """
    geo = Geoserver(
        GEOSERVER_URL,
        username=username,
        password=password,
    )

    first_layer = fiona.listlayers(gpkg_path)[0]
    store_name = upload_geopackage_to_geoserver(
        gpkg_path,
        username,
        password,
        workspace=workspace,
    )
    geo.delete_layer(first_layer, workspace=workspace)
    for layer in layers:
        geo.publish_featurestore(store_name, layer)

    if style_dict:
        for layer, sld_path in style_dict.items():
            sld_name = os.path.splitext(os.path.basename(sld_path))[0]
            if os.path.isfile(sld_path):
                with open(sld_path, "rb") as f:
                    sld_data = f.read()
            else:
                sld_path = f"https://raw.githubusercontent.com/SeaBee-no/annotation/main/sld_files/{sld_path}"
                try:
                    response = requests.get(sld_path)
                    response.raise_for_status()
                    sld_data = response.content
                except requests.exceptions.RequestException as e:
                    print(
                        f"ERROR: Unable to retrieve SLD file '{sld_name}' from GitHub. {e}"
                    )
                    continue

            try:
                geo.upload_style(path=sld_data, name=sld_name, workspace=workspace)
            except GeoserverException as e:
                if "already exists" in str(e):
                    print(
                        f"WARNING: Style '{sld_name}' already exists. The old style will be used for layer '{layer}'.\n"
                        "If you want to use a different style, either delete/update the existing version, or create an SLD file with a different name."
                    )
                else:
                    print(f"Error: Unable to upload style. {e}")
                    continue

            geo.publish_style(
                layer_name=layer, style_name=sld_name, workspace=workspace
            )

    return store_name


def upload_raster_to_geoserver(
    fpath, user, password, workspace="geonode", sld_name=None
):
    """Upload a raster from JupyterHub to GeoServer. The layer name in
    GeoServer will be the file name minus the extension.

    NOTE: The GeoServer layer will be overwritten if it already exists.

    Args
        fpath:     Str. Path to raster dataset to be uploaded
        user:      Str. GeoServer admin. user
        password:  Str. GeoServer admin. password
        workspace: Str. Default 'geonode'. GeoServer workspace
        sld_name:  Str or None. Default None. The name of one of the raster styles
                   defined here:
                       https://github.com/SeaBee-no/annotation/tree/main/sld_files
                   (e.g. 'rgb_default_rgb'). WITHOUT the '.sld' extension. The SLD
                   files define which bands to display in which colours, and whether
                   to apply normalisation etc. If None, the first three bands will
                   be coloured R, G, B without normalisation.

    Returns
        None.
    """
    if sld_name:
        if sld_name.endswith(".sld"):
            sld_name = os.path.splitext(sld_name)[0]

    # Authenticate
    geo = Geoserver(
        GEOSERVER_URL,
        username=user,
        password=password,
    )

    # Upload
    fname = os.path.basename(fpath)
    layer_name = os.path.splitext(fname)[0]
    geo.create_coveragestore(
        layer_name=layer_name,
        path=fpath,
        workspace=workspace,
    )

    # Apply style if desired
    if sld_name:
        sld_path = f"https://raw.githubusercontent.com/SeaBee-no/annotation/main/sld_files/{sld_name}.sld"
        try:
            response = requests.get(sld_path)
            response.raise_for_status()
            sld_data = response.content
        except requests.exceptions.RequestException as e:
            print(f"ERROR: Unable to retrieve SLD file '{sld_name}' from GitHub. {e}")
            return
        try:
            geo.upload_style(path=sld_data, name=sld_name, workspace=workspace)
        except GeoserverException as e:
            if "already exists" in str(e):
                print(
                    f"WARNING: Style '{sld_name}' already exists. The old style will be used for layer '{layer_name}'.\n"
                    "If you want to use a different style, either delete/update the existing version, or create an SLD file with a different name."
                )
            else:
                print(f"Error: Unable to upload style. {e}")
                return

        geo.publish_style(
            layer_name=layer_name, style_name=sld_name, workspace=workspace
        )


def get_raster_sld(tif_path, enhance_contrast=None):
    """Get the name of a default SeaBee raster style (.sld) based on the numer of
    bands in the dataset and whether or not to apply contrast enhancement.

    Default SeaBee styles (SLDs) for vector and raster data are hosted here:

        https://github.com/SeaBee-no/annotation/tree/main/sld_files

    Args
        tif_path:         Str. Path to standardised GeoTIFF.
        enhance_contrast: Str or None. Default None. Whether to apply contrast
                          enhancement to the display bands. Valid choices are
                          None, 'normalise' or 'histogram'.

    Returns
        Str. Name of SLD file to use WITHOUT the .sld extension (which can be
        passed to 'upload_raster_to_geoserver').

    Raises
        ValueError if 'enhance_contrast' not in (None, 'normalise', 'histogram').
    """
    if enhance_contrast not in (None, "normalise", "histogram"):
        raise ValueError(
            "'enhance_contrast' must be one of (None, 'normalise', 'histogram')."
        )
    nbands = get_geotiff_info(tif_path)["num_bands"]
    if enhance_contrast:
        sld_name = f"{nbands}band_{enhance_contrast}_rgb"
    else:
        sld_name = f"{nbands}band_default_rgb"

    return sld_name


def publish_to_geonode(
    layer_name,
    user,
    password,
    workspace="geonode",
    store_name=None,
    wait=10,
):
    """Publish a layer from GeoServer to GeoNode.

    Args
        layer_name: Str. Name of layer to be published
        user:       Str. GeoNode admin. user
        password:   Str. GeoNode admin. password
        workspace:  Str. Default 'geonode'. GeoServer workspace
        store_name: Str or None. Default None. Name of store on GeoServer. For
                    rasters (e.g. .tifs), the store name is the same as the layer
                    name. Either pass 'store_name=layer_name' explicitly, or just
                    leave 'store_name=None' and the function will assume
                    'store_name=layer_name' by default. For vector data (e.g. from
                    a geopackage), the store is the name of the geopackage and the
                    layer is the name of the layer within the geopackage.
        wait:       Int. Default 10. Time in seconds to wait between
                    progress updates.

    Returns
        None. Raster layer is published.
    """
    cmd_url = GEONODE_URL + r"management/commands/"
    status_url = GEONODE_URL + r"management/jobs/"
    header = {"Content-Type": "application/json"}
    command = "updatelayers"
    if store_name is None:
        kwargs = {"filter": layer_name, "store": layer_name, "workspace": workspace}
    else:
        kwargs = {"filter": layer_name, "store": store_name, "workspace": workspace}
    auth = (user, password)
    response = requests.post(
        cmd_url,
        headers=header,
        auth=auth,
        data=json.dumps({"command": command, "kwargs": kwargs}),
    )
    response.raise_for_status()

    # Wait for completion
    job_id = response.json()["data"]["id"]
    job_url = status_url + f"{job_id}/status/"
    job_status = "NOT_FINISHED"
    while job_status != "FINISHED":
        job_status = requests.get(job_url, auth=auth).json()["status"]
        time.sleep(wait)


def get_dataset_by_title(title):
    """Get a dataset from GeoNode by title.

    Args
        title: Str. Title of dataset to search for.

    Returns
        Dict. Dataset information.
    """
    filter_url = GEONODE_URL + "datasets?filter{title}=" + title
    response = requests.get(filter_url)
    response.raise_for_status()
    data = response.json()
    if data["total"] == 0:
        raise ValueError(f"Dataset with title '{title}' not found.")
    elif data["total"] > 1:
        raise ValueError(f"More than one dataset found with title '{title}'.")
    else:
        return data["datasets"][0]


def update_geonode_metadata(layer_name, user, password, metadata):
    """Update metadata for a layer published on GeoNode.

    Args
        layer_name: Str. Path to raster data to be uploaded
        user:       Str. GeoNode admin. user
        password:   Str. GeoNode admin. password
        metadata:   Dict. Dict with metadata attributes as keys

    Returns
        None. Metadata attributes are updated.
    """

    dataset_id = get_dataset_by_title(layer_name)["pk"]

    update_url = GEONODE_URL + f"datasets/{dataset_id}"
    auth = (user, password)
    response = requests.patch(update_url, auth=auth, json=metadata)
    response.raise_for_status()


def get_html_abstract(dir_path):
    """Build an HTML abstract for GeoNode based on data in 'config.seabee.yaml'.

    Args
        dir_path: Str. Path to mission folder.

    Returns
        Str. HTML for abstract.
    """
    group, area, date, spec, elev = ortho.parse_mission_data(dir_path, parse_date=True)
    config_data = ortho.parse_config(dir_path)

    # Set default licence if not specified
    if config_data.get("licence") is None:
        config_data["licence"] = DEFAULT_LICENCE
    if config_data.get("licence_link") is None:
        config_data["licence_link"] = DEFAULT_LICENCE_LINK

    html = pd.DataFrame(
        [
            os.path.join(*storage._jhub_path_to_minio(dir_path)),
            group,
            area,
            date.strftime("%Y-%m-%d"),
            config_data.get("spectrum_type", "-").upper(),
            config_data.get("elevation", "-"),
            config_data["organisation"],
            config_data.get("project", "-"),
            config_data.get("vehicle", "-"),
            config_data.get("sensor", "-"),
            config_data.get("creator_name", "-"),
            config_data["theme"].capitalize(),
            config_data["nfiles"],
            config_data["licence"],
            config_data["licence_link"],
        ],
        index=[
            "MinIO path",
            "Grouping",
            "Area",
            "Flight date",
            "Spectrum",
            "Elevation (m)",
            "Organisation",
            "Project",
            "Vehicle",
            "Sensor",
            "Creator",
            "Theme",
            "N images",
            "Licence",
            "Licence link",
        ],
    ).to_html(header=None)

    abstract = f"Collected by {config_data['organisation']} at {area} ({group}) on {date.strftime('%Y-%m-%d')}.<br><br>{html}"

    return abstract


def get_detection_abstract(
    gdf: gpd.GeoDataFrame,
    parent_layer_name: str,
    model: str,
    jhub_path: str,
    filter_thresh: float,
):
    """Build an HTML abstract for GeoNode based on data in 'config.seabee.yaml' .

    Args
        gdf:               Obj. Geodataframe of detection results.
        parent_layer_name: Str. Name of parent layer in GeoNode.
        model:             Str. Name of model used for detection.
        jhub_path:         Str. jhub path to geopackage file on minio. Will be
                           translated to s3 path.
        filter_thresh:     Float. Threshod used to filter 'gdf' based on 'score_species'.

    Returns
        Str. HTML for abstract.
    """
    mission_name = parent_layer_name.removesuffix("_detections")
    ds_parent = get_dataset_by_title(mission_name)
    summary = pd.DataFrame(
        (gdf.species_norwegian + " (" + gdf.species_english + ")").value_counts(),
        columns=["count"],
    )
    summary.loc["Total Species Count"] = [summary["count"].sum()]
    summary.loc["Geopackage Path"] = os.path.join(
        *storage._jhub_path_to_minio(jhub_path)
    )
    summary.loc["Orthophoto Name"] = f"{mission_name}.tif"
    summary.loc["Orthophoto Link"] = (
        f"https://geonode.seabee.sigma2.no/catalogue/#/dataset/{ds_parent['pk']}"
    )
    abstract = (
        f"Detections using model '{model}' on {mission_name}. "
        f"Only detections with species confidence ≥ {filter_thresh} are shown."
        f"<br><br>{summary.to_html(header=None)}.<br>"
    )
    abstract += f"Parent dataset summary .<br><br>{ds_parent['abstract']}"

    return abstract


def upload_document_to_geonode(file_path, doc_name, doc_title, username, password):
    """
    Uploads a document (PDF, image, text file, Word document, video file) to GeoNode.

    NOTE: This endpoint is not currently supported by our version of GeoNode. When we
    upgrade to 4.1 this code needs testing!

    Args
        file_path: Str. The path to the file to be uploaded.
        doc_name: Str. The name of the document to create on GeoNode.
        doc_title: Str. The title to use for the document on GeoNode.
        username: Str. Admin. username for GeoNode.
        password: Str. Admin. password for GeoNode.

    Returns
        None.

    Raises
        ValueError if 'file_path' does not exist.
        ValueError if the MIME type cannot be determined.
        RequestException if the request fails.
    """
    if not os.path.isfile(file_path):
        raise ValueError(f"'{file_path}' does not exist.")

    mime_type = mimetypes.guess_type(file_path)[0]
    if mime_type is None:
        raise ValueError(f"Could not determine MIME type for '{file_path}'.")

    payload = {"title": doc_title}
    files = [("doc_file", (doc_name, open(file_path, "rb"), mime_type))]
    auth = (username, password)
    url = os.path.join(GEONODE_URL, "documents")

    try:
        response = requests.request("POST", url, auth=auth, data=payload, files=files)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while uploading the file: {e}")


def geodataframe_to_raster(
    gdf, value_col, template_raster_path, output_raster_path, window_size=50000
):
    """Convert a polygon geodataframe to a single band integer raster based on a
    template raster and a column in the attribute table.

    Args:
        gdf (gpd.GeoDataFrame): Polygons to rasterize.
        value_col (str): Name of column in 'gdf' containing integer values for each class.
        template_raster_path (str): Path to GeoTIFF to use as the "template raster".
        output_raster_path (str): Categorical GeoTIFF to create.
        window_size (int): Size of the processing window.

    Returns:
        None. Integer raster saved to 'output_raster_path'.

    Raises:
        KeyError: If 'value_col' not in columns of 'gdf'.
        ValueError: If 'window_size' is not an integer.

        Prints a warning if the CRS of 'gdf' does not match that of 'template_raster_path'.
        In this case, 'gdf' is reprojected before rasterizing.
    """
    if value_col not in gdf.columns:
        raise KeyError(f"Column '{value_col}' not found in columns of 'gdf'.")
    gdf[value_col] = gdf[value_col].astype(int)

    if not isinstance(window_size, int):
        raise ValueError("'window_size' must be an integer.")

    with rio.open(template_raster_path) as src:
        template_meta = src.meta.copy()
        crs = src.crs

    if gdf.crs != crs:
        print(
            "WARNING: CRS of 'gdf' does not match that of 'template_raster_path'. "
            "'gdf' will be reprojected."
        )
        gdf = gdf.to_crs(crs)

    # Process in chunks of size window_size x window_size
    template_meta.update({"count": 1, "dtype": rio.int32, "compress": "lzw"})
    with rio.open(output_raster_path, "w", **template_meta) as dst:
        for i, j in product(
            range(0, template_meta["height"], window_size),
            range(0, template_meta["width"], window_size),
        ):
            # Adjust window size to avoid going out of bounds
            win_height = min(window_size, template_meta["height"] - i)
            win_width = min(window_size, template_meta["width"] - j)
            window = Window(j, i, win_width, win_height)

            # Rasterize the current window
            out_shape = (window.height, window.width)
            shapes = (
                (geom, value) for geom, value in zip(gdf.geometry, gdf[value_col])
            )
            raster = rasterize(
                shapes=shapes,
                out_shape=out_shape,
                transform=src.window_transform(window),
                fill=0,
                dtype=rio.int32,
            )

            # Write to output raster
            dst.write(raster, 1, window=window)
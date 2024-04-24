import json
import mimetypes
import os
import subprocess
import time

import fiona
import geopandas as gpd
import pandas as pd
import rasterio as rio
import requests
from geo.Geoserver import Geoserver, GeoserverException
from rasterio.enums import ColorInterp

from . import ortho, storage

GEOSERVER_URL = os.environ.get(
    "GEOSERVER_URL", r"https://geonode.seabee.sigma2.no/geoserver"
)
GEONODE_URL = os.environ.get("GEONODE_URL", r"https://geonode.seabee.sigma2.no/api/v2/")
DEFAULT_BAND_ORDER = ["nir", "rededge", "red", "green", "blue"]


def get_geotiff_info(tif_path):
    """Read basic metadata from a GeoTiff.

    Args
        tif_path: Str. Path to GeoTiff.

    Returns
        Dict of properties. E.g.:
            {
                "pixel_dtype": "uint8",
                "num_bands": 4,
                "band_descriptions": {"red": 1, "green": 2, "blue": 3},
                "nodata_value": None,
            }

    Raises
        ValueError if the GeoTiff has multiple NoData values.
    """
    with rio.open(tif_path) as src:
        nbands = src.count
        band_descriptions = {
            desc.lower(): idx + 1 for idx, desc in enumerate(src.descriptions) if desc
        }
        colour_interps = {
            colorinterp.name.lower(): idx + 1
            for idx, colorinterp in enumerate(src.colorinterp)
            if colorinterp.name
        }

        # Only use band info if each band is uniquely identified. Try 'descriptions'
        # first, then fall back to 'colorinterp'
        if len(band_descriptions) == nbands:
            band_info = band_descriptions
        elif len(colour_interps) == nbands:
            band_info = colour_interps
        else:
            band_info = None

        info_dict = {
            "pixel_dtype": src.dtypes[0],
            "num_bands": nbands,
            "band_descriptions": band_info,
        }

        nodata_values = set(nodata for nodata in src.nodatavals)
        if len(nodata_values) == 1:
            info_dict["nodata_value"] = nodata_values.pop()
        else:
            raise ValueError(
                f"'{tif_path}' has multiple NoData values: {nodata_values}."
            )

    return info_dict


def rename_key(d, old_key, new_key):
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


def patch_geotiff_info(info_dict):
    """If accurate metadata cannot be read directly from a GeoTIFF, this function
    attempts to fill-in some sensible defaults.

    Args
        info_dict: Dict. As returned by 'get_geotiff_info'.

    Returns
        Dict. Missing data in 'info_dict' is patched/updated with default values.

    Raises
        ValueError if the band order cannot be inferred from the number of bands.
    """
    # Assume default bands if not explicitly provided
    band_dict = info_dict.get("band_descriptions")
    if band_dict is None:
        if info_dict.get("num_bands") == 4:
            # Assume RGBA
            info_dict["band_descriptions"] = {"red": 1, "green": 2, "blue": 3}
        elif info_dict["num_bands"] == 5:
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
            raise ValueError(f"Could not determine correct band order for '{in_tif}'.")

    # Standardise 're' to 'rededge'
    rename_key(info_dict["band_descriptions"], "re", "rededge")

    nodata = info_dict.get("nodata_value")
    if nodata is None:
        # Assume 0
        info_dict["nodata_value"] = 0

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
            f"Currently supported bands are 'nir', 'rededge', 'red', 'green' and 'blue'. Got {band_order}."
        )

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
        in_tif,
        out_tif,
    ]
    for band in band_order[::-1]:
        if band in band_dict:
            cmd.insert(1, str(band_dict[band]))
            cmd.insert(1, "-b")

    subprocess.check_call(cmd)

    # Explicitly set band info and colorinterp
    color_interp_dict = {
        "red": ColorInterp.red,
        "green": ColorInterp.green,
        "blue": ColorInterp.blue,
    }
    descriptions = [band for band in band_order if band in band_dict]
    colorinterps = [
        color_interp_dict.get(band, ColorInterp.grey) for band in descriptions
    ]
    with rio.open(out_tif, "r+") as ds:
        for bidx in range(ds.count):
            ds.set_band_description(bidx + 1, descriptions[bidx])
        ds.colorinterp = tuple(colorinterps)


def set_nodata_from_alpha(
    in_tif, out_tif, nodata_value=0, reclass_value=1, alpha_band_nodata=0
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
        nodata_value:      Int. Default 0. Value to set as 'nodata' in the raster.
        reclass_value:     Int. Default 1. Value to assign to valid data that is
                           equal to the new 'nodata_value'.
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
        "nodata_value": nodata_value,
        "reclass_value": reclass_value,
        "alpha_band_nodata": alpha_band_nodata,
    }
    for var_name, val in variables.items():
        if not isinstance(val, int):
            raise ValueError(f"'{var_name}' must be an integer.")
        if not (0 <= val <= 255):
            raise ValueError(f"'{var_name}' must be between 0 and 255.")

    with rio.open(in_tif) as src:
        data = src.read()

        # Set valid values that are equal to the new 'nodata_value' to the
        # 'reclass_value'
        data[:-1][data[:-1] == nodata_value] = reclass_value

        # Set band values to 'nodata_value' where the alpha band is equal to
        # 'alpha_band_nodata'
        alpha_band_mask = data[-1] == alpha_band_nodata
        for band in range(data.shape[0] - 1):
            data[band][alpha_band_mask] = nodata_value

        # Save
        profile = src.profile
        profile.update(compress="LZW", BIGTIFF="YES")

        with rio.open(out_tif, "w", **profile) as dst:
            dst.write(data)
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
    # Read basic metadata
    info_dict = get_geotiff_info(in_tif)

    # Patch missing metadata with default values
    info_dict = patch_geotiff_info(info_dict)

    # Explicitly set NoData as zero based on alpha mask
    temp_fold = os.path.split(out_tif)[0]
    temp_tif = os.path.join(temp_fold, "temp.tif")
    fname = os.path.basename(in_tif)
    if fname.lower().startswith("pix4d"):
        # Some Pix4D mosaics seem to have NoData cells equal to 0 that are not
        # included in the alpha mask. This is either an error in Pix4D or a
        # problem with some of the manual post-processing. Assume band values
        # of zero are also NoData.
        reclass_value = 0
    else:
        # Band values of zero in the ODM output seem genuine, so preserve them
        # by reclassifying to 1.
        reclass_value = 1
    set_nodata_from_alpha(
        in_tif,
        temp_tif,
        nodata_value=0,
        reclass_value=reclass_value,
        alpha_band_nodata=0,
    )

    # Restructure orthophoto
    band_dict = info_dict["band_descriptions"]
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
                        "If you want to use a different style, either delete/update the existing version, or create an SLD file with a different name.\n"
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
                    "If you want to use a different style, either delete/update the existing version, or create an SLD file with a different name.\n"
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
    assert data["total"] == 1, f"More than one dataset found with title '{title}'."
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
            config_data.get("creator_name", "-"),
            config_data["theme"].capitalize(),
            config_data["nfiles"],
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
            "Creator",
            "Theme",
            "N images",
        ],
    ).to_html(header=None)

    abstract = f"Collected by {config_data['organisation']} at {area} ({group}) on {date.strftime('%Y-%m-%d')}.<br><br>{html}"

    return abstract


def get_detection_abstract(
    gdf: gpd.GeoDataFrame, parent_layer_name: str, model: str, jhub_path: str
):
    """Build an HTML abstract for GeoNode based on data in 'config.seabee.yaml' .

    Args
        dir_path: Str. Path to mission folder.
        parent_layer_name: Str. Name of parent layer in GeoNode.
        model:    Str. Name of model used for detection.
        jhub_path: Str. jhub path to geopackage file on minio. Will be translated to s3 path

    Returns
        Str. HTML for abstract.
    """

    ds_parent = get_dataset_by_title(parent_layer_name)

    summary = pd.DataFrame(
        (gdf.species_norwegian + "(" + gdf.species_english + ")").value_counts(),
        columns=["count"],
    )
    summary.loc["Total Species Count"] = [summary["count"].sum()]
    summary.loc["Geopackage Path"] = os.path.join(
        *storage._jhub_path_to_minio(jhub_path)
    )
    summary.loc["Orthophoto Name"] = parent_layer_name
    summary.loc["Orthophoto Link"] = (
        f"https://geonode.seabee.sigma2.no/catalogue/#/dataset/{ds_parent['pk']}"
    )

    abstract = f"Detection using {model} on {parent_layer_name}.<br><br>{summary.to_html(header=None)}.<br>"
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
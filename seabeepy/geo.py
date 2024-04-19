import json
import os
import subprocess
import time

import fiona
import geopandas as gpd
import pandas as pd
import requests
from geo.Geoserver import Geoserver, GeoserverException

from . import ortho, storage

GEOSERVER_URL = os.environ.get(
    "GEOSERVER_URL", r"https://geonode.seabee.sigma2.no/geoserver"
)
GEONODE_URL = os.environ.get("GEONODE_URL", r"https://geonode.seabee.sigma2.no/api/v2/")


def standardise_orthophoto(
    in_tif, out_tif, red_band=1, green_band=2, blue_band=3, nodata=255
):
    """Create a 3-band, cloud-optimised GeoTIFF ready for upload to GeoServer.
    This function is useful to ensure raster datasets uploaded to GeoServer are
    consistent, regardless of who produced them with which software.

    Builds an RGB composite from the specified bands from 'in_tif'. Bands are
    converted to 8-bit (with value scaling), any alpha bands are removed and
    existing overview layers are discarded and rebuilt. The file is saved using
    LZW compression.

    Args
        in_tif:     Str. Path to original GeoTIFF
        out_tif:    Str. Path to GeoTIFF to be created. Must be a folder where you
                    have "write" access i.e. somewhere in your HOME directory
        red_band:   Int. Default 1. Band number for red band in 'in_tif'
        green_band: Int. Default 2. Band number for green band in 'in_tif'
        blue_band:  Int. Default 3. Band number for blue band in 'in_tif'
        nodata:     Int. Default 255. Value to use for NoData. Typically 255 for
                    seabirds and 0 for habitat mapping.

    Returns
        None. Raster is saved to the specified path.
    """
    for band in (red_band, green_band, blue_band):
        if not isinstance(band, int):
            raise ValueError(
                "'red_band', 'green_band' and 'blue_band' must all be integers."
            )

    assert isinstance(nodata, int) and (
        0 <= nodata <= 255
    ), "'nodata' must be an integer between 0 and 255."

    cmd = [
        "gdal_translate",
        "-b",
        str(red_band),
        "-b",
        str(green_band),
        "-b",
        str(blue_band),
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
    subprocess.check_call(cmd)


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


def upload_raster_to_geoserver(fpath, user, password, workspace="geonode"):
    """Upload a raster from JupyterHub to GeoServer. The layer name in
    GeoServer will be the file name minus the extension.

    NOTE: The GeoServer layer will be overwritten if it already exists.

    Args
        fpath:     Str. Path to raster dataset to be uploaded
        user:      Str. GeoServer admin. user
        password:  Str. GeoServer admin. password
        workspace: Str. Default 'geonode'. GeoServer workspace

    Returns
        None.
    """
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
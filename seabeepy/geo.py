import json
import os
import subprocess
import time

import pandas as pd
import geopandas as gpd
import requests
from geo.Geoserver import Geoserver, GeoserverException

from . import ortho, storage

GEOSERVER_URL = os.environ.get("GEOSERVER_URL", r"https://geonode.seabee.sigma2.no/geoserver")
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


def upload_geopackage_to_geoserver(fpath: str, user: str, password: str, workspace="geonode") -> str:
    """Upload a geopackage from JupyterHub to GeoServer. The filename will be used
    as datastore name while the layer in the file will be used as layer name

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
    
    url = f"{GEOSERVER_URL}/rest/workspaces/{workspace}/datastores/{store_name}/file.gpkg"

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


def publish_to_geonode(layer_name, user, password, workspace="geonode", wait=10):
    """Publish a layer from GeoServer to GeoNode.

    Args
        layer_name: Str. Name of layer to be published
        user:       Str. GeoNode admin. user
        password:   Str. GeoNode admin. password
        workspace:  Str. Default 'geonode'. GeoServer workspace
        wait:       Int. Default 10. Time in seconds to wait between
                    progress updates.

    Returns
        None. Raster layer is published.
    """
    cmd_url = GEONODE_URL + r"management/commands/"
    status_url = GEONODE_URL + r"management/jobs/"
    header = {"Content-Type": "application/json"}
    command = "updatelayers"
    kwargs = {"filter": layer_name, "store": layer_name, "workspace": workspace}
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

    abstract = f"RGB mosaic collected by {config_data['organisation']} at {area} ({group}) on {date.strftime('%Y-%m-%d')}.<br><br>{html}"

    return abstract


def get_detection_abstract(gdf: gpd.GeoDataFrame, parent_layer_name: str,  model: str, jhub_path: str):
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

    summary = pd.DataFrame((gdf.species_norwegian + "(" + gdf.species_english + ")").value_counts(), columns=["count"])
    summary.loc["Total Species Count"] = [summary["count"].sum()]  
    summary.loc["Geopackage Path"] = os.path.join(*storage._jhub_path_to_minio(jhub_path))
    summary.loc["Orthophoto Name"] = parent_layer_name
    summary.loc["Orthophoto Link"] = GEONODE_URL + f"datasets/{ds_parent['pk']}"
    
    abstract = f"Detection using {model} on {parent_layer_name}.<br><br>{summary.to_html(header=None)}<br>"
    abstract +=f"Parent dataset summary.<br><br>{ds_parent['abstract']}"
    return abstract
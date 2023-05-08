import json
import os
import subprocess
import time

import requests
from geo.Geoserver import Geoserver

GEOSERVER_URL = r"https://geonode.seabee.sigma2.no/geoserver"
GEONODE_URL = r"https://geonode.seabee.sigma2.no/api/v2/"


def standardise_orthophoto(in_tif, out_tif, red_band=1, green_band=2, blue_band=3, nodata=255):
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
    
    assert isinstance(nodata, int) and (0 <= nodata <= 255), "'nodata' must be an integer between 0 and 255."

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

    return None


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
        Str. Name of layer added to GeoServer.
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

    return layer_name


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

    return None


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
    filter_url = GEONODE_URL + f"resources?search={layer_name}&search_fields=title"
    response = requests.get(filter_url)
    response.raise_for_status()
    data = response.json()
    assert data["total"] == 1, f"More than one dataset found with title '{layer_name}'."
    dataset_id = data["resources"][0]["pk"]

    update_url = GEONODE_URL + f"datasets/{dataset_id}"
    auth = (user, password)
    response = requests.patch(update_url, auth=auth, json=metadata)
    response.raise_for_status()

    return None
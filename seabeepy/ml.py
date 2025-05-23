import os
import subprocess
from datetime import datetime
from pathlib import Path

import geopandas as gpd
import pandas as pd
import yaml
from sqlalchemy import text

from . import geo, ortho, storage

# NR's container will try to use the device below if torch.cuda.is_available()
# returns True. Otherwise it will default to 'cpu'. Set to 'cuda' for Sigma2 GPUs
DEVICE = "cuda"
ROOT_PATH = "/home/notebook/shared-seabee-ns9879k"  # Mount path for MinIO
VALID_TASKS = ("detection", "segmentation")
VALID_THEMES = ("seabirds", "mammals", "habitat")
DEFAULT_TASKS = {
    "seabirds": "detection",
    "mammals": "detection",
    "habitat": "segmentation",
}
BANDS_TO_SPEC = {3: "rgb", 5: "msi"}


def get_ml_options(dir_path):
    """Update default ML options with those specified by the user in
    'config.seabee.yaml'.

    Args
        dir_path: Str. Path to flight directory

    Returns
        Dict of options to pass to NR's machine learning algorithm.
    """
    # Read user options
    config_data = ortho.parse_config(dir_path)
    theme = config_data["theme"].lower()
    user_options = config_data.get("ml_options", {})

    # Define default options
    default_options = {"task": DEFAULT_TASKS[theme], "model": None}

    # Update default options with user options
    default_options.update(user_options)

    # If no model is specified, use the most recent model for the task
    if default_options["model"] is None:
        default_options["model"] = get_default_model(
            dir_path, default_options["task"], theme
        )

    return default_options


def get_default_model(dir_path, task, theme):
    """Get the most recent model for 'task' based on the date in the model name, the
    number of bands in the dataset, and the SeaBee 'theme'.

    Assumes that ML models are named using the following convention:

        {org}_{theme}_{spec}_{YYYYMMDD}.zip

    e.g. 'niva_habitat_rgb_YYYYMMDD.zip'

    Args
        dir_path: Str. Path to flight directory.
        task:     Str. 'detection' or 'segmentation'.
        theme:    Str. 'seabirds', 'mammals' or 'habitat'.

    Returns
        Str. The name of the most recent model.

    Raises
        ValueError if 'task' not in VALID_TASKS.
        ValueError if 'theme' not in VALID_THEMES.
        ValueError if the number of bands in the dataset is not 3 or 5 (because we
        don't yet have models to handle these datasets).
        ValueError if a default model cannot be identified.
    """
    if task not in VALID_TASKS:
        raise ValueError(f"'task' must be one of {VALID_TASKS}.")
    if theme not in VALID_THEMES:
        raise ValueError(f"'theme' must be one of {VALID_THEMES}.")

    # Get number of bands in dataset to determine spectrum type
    layer_name = ortho.get_layer_name(dir_path)
    tif_path = os.path.join(dir_path, "orthophoto", f"{layer_name}.tif")
    nbands = geo.get_geotiff_info(tif_path)["num_bands"]
    spec = BANDS_TO_SPEC.get(nbands)
    if spec is None:
        raise ValueError(
            f"Default ML model not yet defined for {nbands}-band datasets."
        )

    # Initialize the most recent date and model
    most_recent_date = datetime.min
    most_recent_model = None

    models_dir = os.path.join(ROOT_PATH, "models", task)
    for filename in os.listdir(models_dir):
        model, _ = os.path.splitext(filename)
        org, model_theme, model_spec, date_str = model.split("_")
        if (model_theme == theme) and (model_spec == spec):
            date = datetime.strptime(date_str, "%Y%m%d")

            # If this date is more recent, update the most recent date and model
            if date > most_recent_date:
                most_recent_date = date
                most_recent_model = model

    if most_recent_model:
        return most_recent_model
    else:
        raise ValueError(
            f"Could not identify default model for {theme} {task} for mission '{dir_path}'."
        )


def write_config_production(
    orthophoto_file: str,
    tmpdir: str,
    model: str,
    task: str,
):
    """'hub.yaml' configures paths to the relevant ML model and data files on the
    JupyterHub. 'image_classification.yaml' configures NR's program for training or
    detection on various types of mission imagery.

    Args
        orthophoto_file: Str. Path to orthophoto to be classified.
        tempdir:         Str. Folder for intermediate files. Must already exist and
                         be a location where the user has write access.
        model:           Str. Name of model to use. See 'models' bucket on MinIO.
        task:            Str. 'detection' or 'segmentation'. The type of
                         classification to perform.

    NOTE: This function needs adapting (and possibly splitting) to handle all the
    different input combinations. I'm not sure what these are yet. Ask Jarle and Are
    to help generalise this function based on their knowledge of the input options.

    Returns
        None. Files are written to {tmpdir}/config/

    Raises
        ValueError if 'task' not in VALID_TASKS.
    """
    if task not in VALID_TASKS:
        raise ValueError(
            f"'task' must be either 'detection' or 'segmentation', not '{task}'."
        )

    # Get model year
    mod_yr = int(model.split("_")[-1][:4])

    # Create 'config' subfolder if it doesn't exist
    config_path = os.path.join(tmpdir, "config")
    os.makedirs(config_path, exist_ok=True)

    # Write Hub config.
    hub_config_path = os.path.join(config_path, "hub.yaml")
    hub_config_data = {
        "DPATH_WORK": f"{tmpdir}/work",
        "DPATH_MODELS": f"{ROOT_PATH}/models",
        "DPATH_RESULTS": f"{tmpdir}/results",
        "DPATH_PRETRAINED": f"{tmpdir}/pretrained",
        "MINIO": {"USE": False},  # MinIO is already mounted, so we can read it directly
        "TEST": {"DEVICE": DEVICE},
    }
    if (mod_yr > 2024) and (task == "detection"):
        # Seabird models from 2025 onwards use the Resnet-101 backbone, which requires additional settings
        hub_config_data["TRAIN"] = {
            "ARCHITECTURE": "fasterrcnn_resnet101_fpn_multitask"
        }
    with open(hub_config_path, "w") as f:
        yaml.dump(hub_config_data, f)

    # Write class config.
    class_config_path = os.path.join(config_path, "image_classification.yaml")
    if task == "detection":
        options = {
            "mode": "production",
            "task": task,
            "score_threshold": 0.1,
            "model": {"id": f"{task}/{model}"},
            "dataset": {
                "root": ROOT_PATH,
                "annotations": {
                    "crs": geo.get_geotiff_info(orthophoto_file)["crs"],
                    "column_main_class": "species",
                    "columns_subtasks": [],
                },
                "test_filenames": [orthophoto_file],
            },
        }
    else:
        # Segmentation
        options = {
            "mode": "production",
            "task": task,
            "model": {
                "id": f"{task}/{model}",
            },
            "dataset": {
                "class_attr": "lev3_name",
                "code_attr": "lev3_code",
                "area_attr": "subareas",
                "root": ROOT_PATH,
                "nodata": int(geo.get_geotiff_info(orthophoto_file)["nodata_value"]),
                "images": {"image_1": {"image_path": orthophoto_file}},
            },
        }
    with open(class_config_path, "w") as f:
        yaml.dump(options, f)


def pretty_run(cmd_list: list[str]):
    """Run a command and print messages."""
    run = subprocess.run(cmd_list, capture_output=True, text=True)
    print(run.stderr)
    print(run.stdout)
    run.check_returncode()


def run_classification_process(
    task: str, process_name: str, config_fold: str, mission_name: str, input_file: str
):
    """Run a specific process in the classification pipeline: pre-processing,
    classification (detection or segmentation), or post-processing.

    Args
        task:         Str. Either 'detection' or 'segmentation'.
        process_name: Str. The name of the process to be run. One of
                      ('preproc', 'test', 'postproc')
        config_fold:  Str. Folder containing configuration files (as generated by
                      'write_config_production').
        mission_name: Str. The name of the mission to be processed.
        input_file:   Str. The input file for the process.

    Returns
        None. The process is run and progress information printed to the screen.

    Raises
        ValueError if 'task' not in VALID_TASKS.
        ValueError if 'process_name' not in ('preproc', 'test', 'postproc').
    """
    if task not in VALID_TASKS:
        raise ValueError(
            f"'task' must be either 'detection' or 'segmentation', not '{task}'."
        )
    if process_name not in ("preproc", "test", "postproc"):
        raise ValueError(
            f"'process_name' must be one of ('preproc', 'test', 'postproc')."
        )
    task = task[:3]
    if (task == "seg") and (process_name == "test"):
        cmd_name = "production"
    else:
        cmd_name = process_name
    print(f"{process_name.capitalize()}...")
    pretty_run(
        [
            f"nrseabee_{task}_{cmd_name}",
            "-c",
            f"{config_fold}/hub.yaml",
            "-o",
            f"{config_fold}/{mission_name}_{process_name}.yaml",
            input_file,
        ]
    )


def run_classification(mission_name: str, config_fold: str, task: str):
    """Run the classification process. A classification run consists of:

         1. Preprocessing the images ('preproc').
         2. Performing the classification ('test' mode).
         3. Post-processing to generate a geopackage containing results as a vector
            layer ('postproc').

    Args
        mission_name: Str. The name of the mission to be processed.
        config_fold:  Str. Folder containing configuration files (as generated by
                      'write_config_production').
        task:         Str. Either 'detection' or 'segmentation'.

    Returns
        None. The standardised orthomosaic in the mission folder is classified and
        progress information printed to the screen.

    Raises
        ValueError if 'task' not in VALID_TASKS.
    """
    if task not in VALID_TASKS:
        raise ValueError(
            f"'task' must be either 'detection' or 'segmentation', not '{task}'."
        )

    try:
        run_classification_process(
            task,
            "preproc",
            config_fold,
            mission_name,
            f"{config_fold}/image_classification.yaml",
        )
        run_classification_process(
            task,
            "test",
            config_fold,
            mission_name,
            f"{config_fold}/{mission_name}_preproc.yaml",
        )
        run_classification_process(
            task,
            "postproc",
            config_fold,
            mission_name,
            f"{config_fold}/{mission_name}_test.yaml",
        )
        print("Classification process completed successfully.")
    except Exception as e:
        print(f"An error occurred during the classification process: {e}")


def is_classification_ready(dir_path: str) -> bool:
    """Check if a standardised ortophoto exists for classification.

    Args
        dir_path: Str. Path to mission folder.

    Returns
        Bool. True if ready for classification, otherwise False.
    """
    layer_name = ortho.get_layer_name(dir_path)

    cog_exists = os.path.isfile(
        os.path.join(dir_path, "orthophoto", f"{layer_name}.tif")
    )

    if cog_exists:
        return True
    else:
        return False


def is_classification_published(dir_path: str) -> bool:
    """Check if results are already published. For 'detection', checks for the
    existence of a standardised geopackage. For 'segmentation' checks for the
    existence of a 'level 1' predictions GeoTiff.

    Args
        dir_path: Str. Path to mission folder.
        task: Str. Task name, for example 'detection'
        model: Str. Model name, a subfolder in the task directory

    Returns
        Bool. True if already published, otherwise False.
    """
    ml_options = get_ml_options(dir_path)
    task = ml_options["task"]
    model = ml_options["model"]
    layer_name = ortho.get_layer_name(dir_path)
    if task == "detection":
        published = os.path.isfile(
            os.path.join(
                dir_path, "results", task, model, f"{layer_name}_detections.gpkg"
            )
        )
    else:
        published = os.path.isfile(
            os.path.join(
                dir_path, "results", task, model, f"{layer_name}_lev1-predictions.tif"
            )
        )
    return published


def check_results_exist(dir_path: str) -> bool:
    """Checks if results already exist for a specific task and ML model.

     Args
        dir_path: Str. Path to mission folder.

    Returns
        True if results already exist, else False.
    """
    ml_options = get_ml_options(dir_path)
    task = ml_options["task"]
    model = ml_options["model"]
    res_dir = os.path.join(dir_path, "results", task, model)
    if os.path.isdir(res_dir):
        return True
    else:
        return False


def get_latest_results_dir(dir_path):
    """Identify the subfolder containing the most recent ML results for a specified
    mission directory.

    Args
        dir_path: Str. Path to mission folder.

    Returns
        Str. Path to most recent results subfolder.
    """
    ml_options = get_ml_options(dir_path)
    task = ml_options["task"]
    model = ml_options["model"]
    res_dir = Path(os.path.join(dir_path, "results", task, model))
    last_res_dir = sorted([p for p in res_dir.iterdir() if p.is_dir()])[-1]

    return last_res_dir


def get_seabirds_file_id(layer_name, eng):
    """Identify the orthophoto ID for the specified layer in the 'seabirds'
    database.

    Args
        layer_name: Str. Name of layer/orthophoto.
        eng:        Obj. Active database connection object connected to the
                    'seabirds' database.

    Returns
        Int. ID of 'layer_name' from the 'files' table in the database.

    Raises
        ValueError if no matching ID can be found.
        ValueError if multiple matching IDs are found.
    """
    if not layer_name.endswith(".tif"):
        layer_name = layer_name + ".tif"

    sql = text("SELECT id from files WHERE filename = :fname")
    file_id_df = pd.read_sql(sql, eng, params={"fname": layer_name})
    if len(file_id_df) == 1:
        return int(file_id_df["id"].iloc[0])
    elif len(file_id_df) == 0:
        raise ValueError(f"No matching file name in the database: '{layer_name}'.")
    else:
        raise ValueError(f"Multiple layers named '{layer_name}' in the database.")


def write_seabird_detections_to_postgis(dir_path, username, password):
    """Write results from machine learning to the 'detections' table in the
    'seabirds' database. Vector polygons are reprojected to WGS84 lat/lon
    before upload.

    NOTE: This function requires the 'files' table to be updated with the latest
    orthophoto details.

    Args
        dir_path: Str. Path to mission folder containing ML results.
        username: Str. Database user with 'write' access.
        password: Str. Database password.

    Returns
        None. Results are added to the 'detections' table.
    """
    eng = storage.connect_postgis(username, password)

    # Get 'fileid' for orthophoto
    layer_name = ortho.get_layer_name(dir_path)
    file_id = get_seabirds_file_id(layer_name, eng)

    # Read results
    res_dir = get_latest_results_dir(dir_path)
    gpkg_path = os.path.join(res_dir, "out.gpkg")
    gdf = gpd.read_file(gpkg_path)

    # Prepare for upload
    gdf = gdf.to_crs("epsg:4326")
    del gdf["TEMP_image_filename"]
    gdf["fileid"] = file_id
    gdf.rename_geometry("geom", inplace=True)

    # Write to database
    # gdf.to_postgis('detections', eng, if_exists='append', index=False)
    print("Results would be written here.")
    print(gdf.head())


def convert_seabird_class_codes_to_names(gdf, username, password):
    """Convert numeric class IDs from the ML to meaningful class names, based on
    information in the 'seabirds' database.

    Args
        gdf:      GeoDataFrame. Raw output from the ML model.
        username: Str. Database username.
        password: Str. Database password.

    Returns
        Copy of 'gdf' with numeric class IDs replaced by class names.
    """
    gdf = gdf.drop(["fileid", "TEMP_image_filename"], axis="columns")
    eng = storage.connect_postgis(username, password)
    tables = ["species"]
    for table in tables:
        gdf[table] = gdf[table].astype(int)
        sql = text(f"SELECT * FROM {table}")
        df = pd.read_sql(sql, eng).add_prefix(f"{table}_")
        gdf[table] = gdf[table].astype(int)
        df[f"{table}_id"] = df[f"{table}_id"].astype(int)
        gdf = gdf.merge(df, left_on=table, right_on=f"{table}_id", how="left").drop(
            [f"{table}_id", table], axis="columns"
        )

    col_order = [
        "individualid",
        "species_norwegian",
        "species_english",
        "species_latin",
        "score_species",
        "visibleonimage",
        "manuallyverified",
        "modelversion",
        "datetimereg",
        "comment",
        "geometry",
    ]
    if "objectness_score" in gdf.columns:
        # 'objectness_score' added to results from recent models. Include if available
        col_order.insert(5, "objectness_score")
    gdf = gdf[col_order]

    return gdf
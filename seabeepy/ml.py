import os
import subprocess
from datetime import datetime

import geopandas as gpd
import pandas as pd
import yaml
from sqlalchemy import create_engine

from . import ortho

# NR's container will try to use the device below if torch.cuda.is_available()
# returns True. Otherwise it will default to 'cpu'. Set to 'cuda' for Sigma2 GPUs
DEVICE = "cuda"
ROOT_PATH = "/home/notebook/shared-seabee-ns9879k"  # Mount path for MinIO
VALID_TASKS = ("detection", "segmentation")


def get_ml_options(dir_path):
    """Update default ML options with those specified by the user in
    'config.seabee.yaml'.

    Args
        dir_path: Str. Path to flight directory

    Returns
        Dict of options to pass to NR's machine learning algorithm.
    """
    # Define default options
    default_options = {"task": "detection", "model": None}

    # Read user options
    config_data = ortho.parse_config(dir_path)
    user_options = config_data.get("ml_options", {})

    # Update default options with user options
    default_options.update(user_options)

    # If no model is specified, use the most recent model for the specified task
    if default_options["model"] is None:
        default_options["model"] = get_default_model(default_options["task"])

    return default_options


def get_default_model(task):
    """Get the most recent model for 'task' based on the date in the model name.

    Args
        task: Str. "detection" or "segmentation".

    Returns
        Str. The name of the most recent model.

    Raises
        ValueError if 'task' not in VALID_TASKS
    """
    if task not in VALID_TASKS:
        raise ValueError(
            f"'task' must be either 'detection' or 'segmentation', not '{task}'."
        )

    # Initialize the most recent date and model
    most_recent_date = datetime.min
    most_recent_model = ""

    models_dir = os.path.join(ROOT_PATH, "models", task)
    for filename in os.listdir(models_dir):
        model = os.path.splitext(filename)[0]
        date_str = model.split("_")[-1]
        date = datetime.strptime(date_str, "%Y%m%d")

        # If this date is more recent, update the most recent date and model
        if date > most_recent_date:
            most_recent_date = date
            most_recent_model = model

    return most_recent_model


def write_config_production(
    orthophoto_file: str,
    tmpdir: str,
    model: str,
    task: str,
    annotations: dict,
):
    """'hub.yaml' configures paths to the relevant ML model and data files on the
    JupyterHub. 'image_detection.yaml' configures NR's program for training or
    detection on various types of mission imagery.

    Args
        orthophoto_file: Str. Path to orthophoto to be classified.
        tempdir:         Str. Folder for intermediate files. Must already exist and
                         be a location where the user has write access.
        model:           Str. Name of model to use. See 'models' bucket on MinIO.
        task:            Str. 'detection' or 'segmentation'. The type of
                         classification to perform.
        annotations:     Dict. Options passed to the classification pipeline. Not
                         sure what is accepted yet - ASK JARLE/ARE. Example:
                             {"crs": "epsg:32632",
                              "column_main_class": "species",
                              "columns_subtasks": ["activity", "sex", "age"],
                             }

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

    # Create 'config' subfolder if it doesn't exist
    config_path = os.path.join(tmpdir, "config")
    os.makedirs(config_path, exist_ok=True)

    hub_config_path = os.path.join(config_path, "hub.yaml")
    with open(hub_config_path, "w") as f:
        yaml.dump(
            {
                "DPATH_WORK": f"{tmpdir}/work",
                "DPATH_MODELS": f"{ROOT_PATH}/models",
                "DPATH_RESULTS": f"{tmpdir}/results",
                "DPATH_PRETRAINED": f"{tmpdir}/pretrained",
                "MINIO": {
                    "USE": False
                },  # MinIO is already mounted, so we can read it directly
                "TEST": {"DEVICE": DEVICE},
            },
            f,
        )

    det_config_path = os.path.join(config_path, "image_detection.yaml")
    with open(det_config_path, "w") as f:
        yaml.dump(
            {
                "mode": "production",
                "task": task,
                "score_threshold": 0.1,
                "model": {"id": f"{task}/{model}"},
                "dataset": {
                    "root": ROOT_PATH,
                    "annotations": annotations,
                    "test_filenames": [orthophoto_file],
                },
            },
            f,
        )


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
        process_name: Str. The name of the process to be run.
        config_fold:  Str. Folder containing configuration files (as generated by
                      'write_config_production').
        mission_name: Str. The name of the mission to be processed.
        input_file:   Str. The input file for the process.

    Returns
        None. The process is run and progress information printed to the screen.

    Raises
        ValueError if 'task' not in VALID_TASKS.
    """
    if task not in VALID_TASKS:
        raise ValueError(
            f"'task' must be either 'detection' or 'segmentation', not '{task}'."
        )
    task = task[:3]
    print(f"{process_name.capitalize()}...")
    pretty_run(
        [
            f"nrseabee_{task}_{process_name}",
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
            f"{config_fold}/image_detection.yaml",
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
        print("Detection process completed successfully.")
    except Exception as e:
        print(f"An error occurred during the detection process: {e}")


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


def is_classification_published(dir_path: str, task: str, model: str) -> bool:
    """Check if a classification geopackage is already published.

    Args
        dir_path: Str. Path to mission folder.
        task: Str. Task name, for example 'detection'
        model: Str. Model name, a subfolder in the task directory

    Returns
        Bool. True if ready to publish, otherwise False.
    """
    layer_name = ortho.get_layer_name(dir_path, model)
    gpkg_exists = os.path.isfile(
        os.path.join(dir_path, "results", task, model, f"{layer_name}.gpkg")
    )
    if gpkg_exists:
        return True
    else:
        return False


def check_results_exist(dir_path: str):
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
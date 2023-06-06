import datetime as dt
import os
import time
from pathlib import Path

import yaml
from schema import And, Optional, Or, Schema, SchemaError
from tqdm.notebook import tqdm


def list_images(image_folder, ext="JPG", verbose=True):
    """Return a list of all images in 'image_fold' with file extension 'ext'.
    Does NOT search the folder recursively. If verbose is True, prints the
    number of images and the total size on disk.

    Args
        image_folder: Str. Folder path to search.
        ext:          Str. Default 'JPG'. Type of files to search for.
        verbose:      Bool. Default True. If True, prints the number of files
                      identified and their total size on disk

    Returns
        List of image paths.
    """
    image_folder = Path(image_folder)
    image_files = list(image_folder.glob(f"*.{ext}"))
    images_size = sum(f.stat().st_size for f in image_files) / 1e9
    if verbose:
        print(
            f"{len(image_files)} files found with a total size of {images_size:.2f} GB."
        )
    image_files = [str(i) for i in image_files]

    return image_files


def show_nodeodm_task_progress_bar(task, update_freq_s=10):
    """Displays a progress bar for a running NodeODM task. Blocks the notebook
    process, but use 'Kernel > Interrupt kernel' if you want to exit the progress
    bar and continue working (without interrupting the task running on NodeODM).

    Args
        task:          Obj. Running NodeODM task object.
        update_freq_s: Int. Default 10. Update frequency for progress bar in
                       seconds.

    Returns
        None. Prints progress and then either completes successfully or shows
        the error reported by NodeODM.
    """
    with tqdm(total=100) as pbar:
        while (task.info().progress < 100) and (task.info().last_error == ""):
            time.sleep(update_freq_s)
            cur_perc = int(task.info().progress)
            pbar.update(cur_perc - pbar.n)
        if task.info().last_error == "":
            print(
                f"Completed successfully in {task.info().processing_time/60000:.1f} minutes."
            )
        else:
            print("Failed with error:")
            print(task.info().last_error)


def get_nodeodm_tasks(node_client):
    """Get current list of NodeODM tasks.

    Args
        node_client: Obj. PyODM client object

    Returns
        List of NodeODM tasks.
    """
    task_ids = node_client.get("task/list")
    task_list = [node_client.get_task(t["uuid"]) for t in task_ids]

    return task_list


def get_nodeodm_options(dir_path):
    """Update default NodeODM options with those specified by the user in 'config.yaml'.

    Args
        dir_path: Str. Path to flight directory

    Returns
        Dict of options to pass to NodeODM.
    """
    # Full list of options here: https://docs.opendronemap.org/arguments/
    default_options = {
        "dsm": True,
        "dtm": True,
        "cog": True,
        "orthophoto-compression": "LZW",
        "orthophoto-resolution": 0.1,  # cm/pixel. If set very small, output will be auto-limited by data to max sensible value
        "dem-resolution": 0.1,  # cm/pixel. If set very small, output will be auto-limited by data to max sensible value
        "max-concurrency": 32,
        "auto-boundary": True,
        "use-3dmesh": True,
        "fast-orthophoto": False,
        "feature-quality": "high",  # ultra | high | medium | low | lowest
        "pc-quality": "high",  # ultra | high | medium | low | lowest
    }

    config_data = parse_config(dir_path)
    if "odm_options" in config_data:
        for key, value in config_data["odm_options"].items():
            default_options[key] = value

    return default_options


def check_config_exists(dir_path):
    """Check whether file 'config.yaml' exists within 'dir_path'.

    Args
        dir_path: Str. Path to flight directory

    Returns
        Bool. True if 'config.yaml' exists, else False.
    """
    if os.path.isfile(os.path.join(dir_path, "config.yaml")):
        return True
    else:
        return False


def check_subdir_exists(dir_path, subdir):
    """Check if subdirectory 'subdir' exists within 'dir_path'.

    Args
        dir_path: Str. Path to flight directory
        subdir:   Str. Name of subdirectory

    Returns
        Bool. True if 'subdir' subdirectory exists, else False.
    """
    if os.path.isdir(os.path.join(dir_path, subdir)):
        return True
    else:
        return False


def check_config_valid(dir_path, verbose=False):
    """Check that information contained in 'config.yaml' can be parsed correctly.

    Args
        dir_path: Str. Path to flight directory
        verbose:  Bool. Default False. Whether to print error details if file is not
                  valid

    Returns
        Bool. True if 'config.yaml' is valid, else False..
    """
    # Define valid schema for 'config.yaml'
    # Full list of options here: https://docs.opendronemap.org/arguments/
    schema = Schema(
        {
            "nfiles": And(int, lambda n: n > 0),
            "organisation": str,
            "mosaic": bool,
            "publish": bool,
            "theme": lambda s: s in ("Seabirds", "Mammals", "Habitat"),
            Optional("creator_name"): Or(str, None),
            Optional("project"): Or(str, None),
            Optional("odm_options"): {
                Optional("dsm"): bool,
                Optional("dtm"): bool,
                Optional("cog"): bool,
                Optional("orthophoto-compression"): lambda s: s
                in ("JPEG", "LZW", "PACKBITS", "DEFLATE", "LZMA", "NONE"),
                Optional("orthophoto-resolution"): Or(int, float),
                Optional("dem-resolution"): Or(int, float),
                Optional("max-concurrency"): int,
                Optional("auto-boundary"): bool,
                Optional("use-3dmesh"): bool,
                Optional("fast-orthophoto"): bool,
                Optional("split"): int,
                Optional("split-overlap"): int,
                Optional("pc-quality"): lambda s: s
                in ("ultra", "high", "medium", "low", "lowest"),
                Optional("feature-quality"): lambda s: s
                in ("ultra", "high", "medium", "low", "lowest"),
            },
        }
    )

    config_path = os.path.join(dir_path, "config.yaml")
    with open(config_path, "r") as stream:
        data = yaml.safe_load(stream)

    try:
        schema.validate(data)
    except SchemaError as e:
        if verbose:
            print("Could not parse 'config.yaml':")
            print(e)

        return False

    return True


def parse_mission_data(mission_name, verbose=False):
    """Extract grouping, area and date from folder name.

    Args
        mission_name: Str. Name of mission folder
        verbose:      Bool. Default False. Whether to print error details
                      if file is not valid

    Returns
        Tuple or Bool. (group, area, date) if name can be parsed, else False.
    """
    try:
        group, area, date = mission_name.split("_")
    except ValueError:
        if verbose:
            print(f"Could not parse '{mission_name}'. Expected (grouping_area_date).")

        return False

    try:
        date = dt.datetime.strptime(date, "%Y%m%d")
    except ValueError:
        try:
            date = dt.datetime.strptime(date, "%Y%m%d%H%M")
        except ValueError:
            if verbose:
                print(
                    f"Could not parse date '{date}'. Expected 'yyyymmdd' or 'yyyymmddHHMM."
                )

            return False

    return (group, area, date)


def parse_config(dir_path):
    """Parse 'config.yaml'.

    Args
        dir_path: Str. Path to mission folder.

    Returns
        Dict.
    """
    config_path = os.path.join(dir_path, "config.yaml")
    with open(config_path, "r") as stream:
        data = yaml.safe_load(stream)

    return data


def check_file_count(dir_path, verbose=False):
    """Count the number of files in 'image_fold' and check it agrees with
    the value in 'config.yaml'.

    Args
        dir_path: Str. Path to mission folder.
        verbose:  Bool. Default False. Whether to print error details if file
                  is not valid

    Returns
        Bool. True if count agrees, else False.
    """
    image_fold = os.path.join(dir_path, "images")
    nfiles_found = len(
        [
            name
            for name in os.listdir(image_fold)
            if os.path.isfile(os.path.join(image_fold, name))
        ]
    )

    config_path = os.path.join(dir_path, "config.yaml")
    with open(config_path, "r") as stream:
        data = yaml.safe_load(stream)
    nfiles_expected = data["nfiles"]

    if nfiles_found == nfiles_expected:
        return True
    else:
        if verbose:
            print(
                f"Number of files in 'images' ({nfiles_found}) does not match the value in 'config.yaml' ({nfiles_expected})."
            )
        return False


def is_publish_ready(dir_path):
    """Check if an original orthophoto is ready to publish. The original orthophoto must be
    in the 'orthophoto' subdirectory and named either 'odm_orthophoto.original.tif' (for
    mosaics generated using NodeODM) or 'pix4d_orthophoto.original.tif' (for mosaics generated
    using Pix4D).

    If an original orthophoto exists, but a standardised version named f'{mission_name}.tif'
    does not, the folder is considered ready for further processing and publishing, if desired.

    NOTE: If the folder contains originals from BOTH ODM and Pix4D, this function will return
    False.

    Args
        dir_path: Str. Path to mission folder.

    Returns
        Bool. True if ready to publish, otherwise False.
    """
    mission_name = os.path.split(dir_path)[-1]

    odm_orig_exists = os.path.isfile(
        os.path.join(dir_path, "orthophoto", "odm_orthophoto.original.tif")
    )
    pix4d_orig_exists = os.path.isfile(
        os.path.join(dir_path, "orthophoto", "pix4d_orthophoto.original.tif")
    )
    cog_exists = os.path.isfile(
        os.path.join(dir_path, "orthophoto", f"{mission_name}.tif")
    )

    # '^' is equivalent to XOR for Bools
    if (odm_orig_exists ^ pix4d_orig_exists) and not cog_exists:
        return True
    else:
        return False

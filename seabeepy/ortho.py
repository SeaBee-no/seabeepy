import datetime as dt
import os
import time
from pathlib import Path

import yaml
from schema import And, Optional, Or, Schema, SchemaError
from tqdm.notebook import tqdm

# Define valid schema for 'config.seabee.yaml'
# Full list of ODM options here: https://docs.opendronemap.org/arguments/
CONFIG_SCHEMA = Schema(
    {
        "grouping": str,
        "area": str,
        "datetime": And(
            str,
            Or(
                lambda date: dt.datetime.strptime(date, "%Y%m%d"),
                lambda date: dt.datetime.strptime(date, "%Y%m%d%H%M"),
            ),
        ),
        "nfiles": And(int, lambda n: n > 0),
        "organisation": str,
        "mosaic": bool,
        "publish": bool,
        "theme": lambda s: s.lower() in ("seabirds", "mammals", "habitat"),
        Optional("spectrum_type"): Or(
            lambda s: s.lower() in ("rgb", "ms", "hsi"), None
        ),
        Optional("elevation"): Or(And(int, lambda x: x >= 0), None),
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
            Optional("pc-rectify"): bool,
            Optional("split"): int,
            Optional("split-overlap"): int,
            Optional("crop"): And(Or(int, float), lambda x: x >= 0),
            Optional("pc-quality"): lambda s: s
            in ("ultra", "high", "medium", "low", "lowest"),
            Optional("feature-quality"): lambda s: s
            in ("ultra", "high", "medium", "low", "lowest"),
        },
    }
)


def list_images(image_folder, verbose=True, check_folders=True):
    """Return a list of all images in 'image_fold' with file extension 'jpg',
    'jpeg' or 'tif' (matched ignoring case). If verbose is True, prints the
    number of images and the total size on disk.

    Args
        image_folder:  Str. Folder path to search.
        verbose:       Bool. Default True. If True, prints the number of files
                       identified and their total size on disk
        check_folders: Bool. Deafult True. Check for images in subfolders at
                       depth 1

    Returns
        List of image paths.
    """
    valid_exts = [".jpg", ".jpeg", ".tif"]
    image_folder = Path(image_folder)
    image_files = [
        img_path
        for img_path in image_folder.glob("*")
        if img_path.suffix.lower() in valid_exts
    ]
    if check_folders:
        image_files.extend(
            [
                img_path
                for img_path in image_folder.glob("*/*")
                if img_path.suffix.lower() in valid_exts
            ]
        )
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
    """Update default NodeODM options with those specified by the user in 'config.seabee.yaml'.

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
    """Check whether file 'config.seabee.yaml' exists within 'dir_path'.

    Args
        dir_path: Str. Path to flight directory

    Returns
        Bool. True if 'config.seabee.yaml' exists, else False.
    """
    if os.path.isfile(os.path.join(dir_path, "config.seabee.yaml")):
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
    """Check that information contained in 'config.seabee.yaml' can be parsed correctly.

    Args
        dir_path: Str. Path to flight directory
        verbose:  Bool. Default False. Whether to print error details if file is not
                  valid

    Returns
        Bool. True if 'config.seabee.yaml' is valid, else False.
    """
    data = parse_config(dir_path)
    try:
        CONFIG_SCHEMA.validate(data)
    except SchemaError as e:
        if verbose:
            print("Could not parse 'config.seabee.yaml':")
            print(e)

        return False

    return True


def parse_mission_data(dir_path, parse_date=False):
    """Extract basic mission info from 'config.seabee.yaml'.

    Args
        dir_path:   Str. Path to flight directory
        parse_date: Bool. Default False. Whether to convert the datetime
                    string to a datetime object

    Returns
        Tuple (group, area, date, spec, elev), where 'spec' and 'elev'
        will be None if not provided.
    """
    # Data already validated by 'check_config_valid', so just extract parts
    data = parse_config(dir_path)
    group = data["grouping"]
    area = data["area"]
    date = data["datetime"]
    spec = data.get("spectrum_type")
    elev = data.get("elevation")

    if parse_date:
        try:
            date = dt.datetime.strptime(date, "%Y%m%d")
        except ValueError:
            date = dt.datetime.strptime(date, "%Y%m%d%H%M")

    return (group, area, date, spec, elev)


def parse_config(dir_path):
    """Parse 'config.seabee.yaml'.

    Args
        dir_path: Str. Path to mission folder.

    Returns
        Dict.
    """
    config_path = os.path.join(dir_path, "config.seabee.yaml")
    with open(config_path, "r") as stream:
        data = yaml.safe_load(stream)

    return data


def get_layer_name(dir_path):
    """Build layer name for GeoServer from basic mission info in 'config.seabee.yaml'.

    Args
        dir_path: Str. Path to flight directory

    Returns
        Str 'group_area_date_[spec]_[elev]' where 'spec' and 'elev' are optional.
        Any spaces in the name will be replaced by '-'.
    """
    group, area, date, spec, elev = parse_mission_data(dir_path, parse_date=False)
    layer_name = "_".join((group, area, date))

    if spec:
        layer_name += f"_{spec}"
    if elev:
        layer_name += f"_{elev}m"

    layer_name = layer_name.replace(" ", "-")

    return layer_name


def check_file_count(dir_path, verbose=False):
    """Count the number of files in 'image_fold' and check it agrees with
    the value in 'config.seabee.yaml'.

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
    data = parse_config(dir_path)
    nfiles_expected = data["nfiles"]
    if nfiles_found == nfiles_expected:
        return True

    if verbose:
        print(
            f"Number of files in 'images' ({nfiles_found}) does not match the value in 'config.seabee.yaml' ({nfiles_expected})."
        )

    return False


def is_publish_ready(dir_path):
    """Check if an original orthophoto is ready to publish. The original orthophoto must be
    in the 'orthophoto' subdirectory and named either 'odm_orthophoto.original.tif' (for
    mosaics generated using NodeODM) or 'pix4d_orthophoto.original.tif' (for mosaics generated
    using Pix4D).

    If an original orthophoto exists, but a standardised version named f'{layer_name}.tif'
    does not, the folder is considered ready for further processing and publishing, if desired.

    NOTE: If the folder contains originals from BOTH ODM and Pix4D, this function will return
    False.

    Args
        dir_path: Str. Path to mission folder.

    Returns
        Bool. True if ready to publish, otherwise False.
    """
    layer_name = get_layer_name(dir_path)

    odm_orig_exists = os.path.isfile(
        os.path.join(dir_path, "orthophoto", "odm_orthophoto.original.tif")
    )
    pix4d_orig_exists = os.path.isfile(
        os.path.join(dir_path, "orthophoto", "pix4d_orthophoto.original.tif")
    )
    cog_exists = os.path.isfile(
        os.path.join(dir_path, "orthophoto", f"{layer_name}.tif")
    )

    # '^' is equivalent to XOR for Bools
    if (odm_orig_exists ^ pix4d_orig_exists) and not cog_exists:
        return True
    else:
        return False

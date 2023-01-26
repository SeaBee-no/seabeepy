import time
from pathlib import Path
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

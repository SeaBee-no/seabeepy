import os
from pathlib import Path

import s3fs


def minio_login(user, password):
    """Login to MinIO using s3fs.

    Args
        access_key: Str. Personal access ID for MinIO. Usually a user's
                    e-mail address
        secret_key: Str. Personal secret key (i.e. password) for MinIO

    Returns
        s3fs client object.
    """
    client = s3fs.S3FileSystem(
        key=user,
        secret=password,
        endpoint_url="https://storage.seabee.sigma2.no",
        config_kwargs={
            "read_timeout": 300,
        },
    )

    return client


def _jhub_path_to_minio(abs_path: str):
    """For files on MinIO (i.e. everything within the 'shared-seabee-ns9879k' folder
    on JuyterHub), converts an absolute file path from JupyterHub into a bucket name
    and object name (for use with the MinIO client).

    Args
        abs_path: Str. Absolute path from JupyterHub to a file or folder on MinIO
                  (i.e. within the 'shared-seabee-ns9879k' folder) or absolute path
                  to a minio location

    Returns
        Tuple of strings (bucket_name, object_name) if file is on MinIO, else
        (None, None).
    """
    bucket_idx = 0
    path_parts = [p for p in abs_path.split("/") if p]
    
    if "shared-seabee-ns9879k" in path_parts:
        bucket_idx = path_parts.index("shared-seabee-ns9879k") + 1

    elif abs_path.startswith("/home/notebook"):
        return (None, None)

    if len(path_parts) > 1:
        bucket_name = path_parts[bucket_idx]
        obj_name = "/".join(path_parts[bucket_idx + 1 :])

        return (bucket_name, obj_name)

    return (None, None)


def copy_file(src_path, dst_path, client, overwrite=False):
    """Convenience function for copying files to MinIO. 'src_path' can be anything the
    user had read access to; 'dst_path' must be a location on MinIO.

    Args
        src_path:  Str. Path to source file on JupyterHub
        dst_path:  Str. Path to destination file on MinIO from JupyterHub (i.e. something
                   within the 'shared-seabee-ns9879k' folder)
        client:    Obj. Active s3fs Python client (from the 'minio_login' function)
        overwrite: Bool. Default False. Whether to overwrite 'dst_path' if it already
                   exists

    Returns
        s3fs result object. Source file is copied to destination.
    """
    src_bucket, src_name = _jhub_path_to_minio(src_path)
    dst_bucket, dst_name = _jhub_path_to_minio(dst_path)

    if dst_bucket is None:
        raise OSError(f"Could not identify destination '{dst_path}' on MinIO.")

    dst_path = os.path.join(dst_bucket, dst_name)
    if client.exists(dst_path) and not overwrite:
        raise OSError(
            f"Destination file '{dst_path}' already exists. Pass 'overwrite = True' to replace."
        )

    if src_bucket:
        # Source file is on MinIO, so use 'cp' as it's faster
        src_path = os.path.join(src_bucket, src_name)
        if not client.isfile(src_path):
            raise OSError(f"Source file '{src_path}' is not a file.")
        result = client.cp(src_path, dst_path)
    else:
        # Source file is not on MinIO
        if not os.path.isfile(src_path):
            raise OSError(f"Source file '{src_path}' is not a file.")
        result = client.put(src_path, dst_path)

    return result


def delete_file(fpath, client):
    """Delete a file on MinIo.

    Args
        fpath:  Str. Absolute path to object from JupyterHub
        client: Obj. Active s3fs Python client (from the 'minio_login' function)

    Returns
        s3fs result object
    """
    bucket, name = _jhub_path_to_minio(fpath)
    if bucket is None:
        raise OSError(f"'{fpath}' is not a file on MinIO.")
    else:
        fpath = os.path.join(bucket, name)
        result = client.rm(fpath)

    return result


def delete_folder(folder, client):
    """Delete a folder and all contents on MinIO. Note that if parent directory of
    'folder' only contains 'folder' (i.e. the parent will become empty after
    'folder' is removed), then the parent folder is also removed. This is just how
    S3 works.

    Args
        folder: Str. Absolute path to MinIO folder from JupyterHub
        client: Obj. Active s3fs Python client (from the 'minio_login' function)

    Returns
        None. Folder is deleted
    """
    folder = folder.rstrip(os.sep)
    bucket, name = _jhub_path_to_minio(folder)
    if bucket is None:
        raise OSError(f"'{folder}' is not a location on MinIO.")

    folder = os.path.join(bucket, name)
    if not client.isdir(folder):
        raise OSError(f"'{folder}' is not a directory.")

    result = client.rm(folder, recursive=True)

    return result


def copy_folder(src_fold, dst_fold, client, overwrite=False, containing_folder=True):
    """Copy everything in 'src_fold' to 'dst_fold', maintaining the subfolder structure
    within 'src_fold'. 'src_fold' can be anything the user had read access to;
    'dst_fold' must be a location on MinIO (both expressed as absolute paths on the Hub).

    If 'containing_folder' is True, 'src_fold' itself will be copied into 'dst_fold'. If
    False, the contents of 'src_fold' will be copied into 'dst_fold'.

    Args
        src_fold:          Str. Absolute source path to folder on SeaBee's JupyterHub
        dst_fold:          Str. Absolute destination folder on MinIO (i.e. something
                           within the 'shared-seabee-ns9879k' folder)
        client:            Obj. Active s3fs Python client (from the 'minio_login' function)
        overwrite:         Bool. Default False. Whether to overwrite 'dst_path' if it
                           already exists
        containing_folder: Bool. Default True. If True, 'src_fold' itself will be copied
                           into 'dst_fold'; if False, the contents of 'src_fold' will be
                           copied

    Returns
        None. Folder and contents are copied.
    """
    src_fold = src_fold.rstrip(os.sep)
    dst_fold = dst_fold.rstrip(os.sep)
    src_bucket, src_name = _jhub_path_to_minio(src_fold)
    dst_bucket, dst_name = _jhub_path_to_minio(dst_fold)

    if dst_bucket is None:
        raise OSError(f"Could not identify destination '{dst_fold}' on MinIO.")

    if containing_folder:
        dst_fold = os.path.join(dst_bucket, dst_name, os.path.basename(src_fold))
    else:
        dst_fold = os.path.join(dst_bucket, dst_name)

    if client.exists(dst_fold) and not overwrite:
        raise OSError(
            f"Destination folder '{dst_fold}' already exists. Pass 'overwrite = True' to replace."
        )

    if client.exists(dst_fold) and overwrite:
        delete_folder(dst_fold, client)

    if src_bucket:
        # Source folder is on MinIO, so use 'cp' as it's faster
        src_fold = os.path.join(src_bucket, src_name)
        if not client.isdir(src_fold):
            raise OSError(f"Source folder '{src_fold}' is not a directory.")
        result = client.cp(src_fold, dst_fold, recursive=True)
    else:
        # Source file is not on MinIO
        if not os.path.isdir(src_fold):
            raise OSError(f"Source folder '{src_fold}' is not a directory.")
        result = client.put(src_fold, dst_fold, recursive=True)

    return result


def copy_nodeodm_results(task_id: str, mission_fold: str, client: s3fs.S3FileSystem) -> bool:
    """NodeODM stores its results in the 'nodeodm-workdir' on MinIO within a folder
    named according to the task's unique ID. This function copies results back to the
    mission folder. This is important as NodeODM periodically deletes everything in
    the 'nodeodm-workdir'.

    Args
        task_id:      Str. Task ID for mission in NodeODM
        mission_fold: Str. Absolute JupyterHub path to mission data.
        client:       Obj. Active MinIO Python client (from the 'minio_login' function)

    Returns
        is_copied:    Bool. If mission bucket orthophoto path is created
    """
    nodeodm_bucket = "nodeodm-workdir"
    task_path = f"{nodeodm_bucket}/{task_id}"
    mission_root = "/".join(_jhub_path_to_minio(mission_fold))

    # Copy folders into agreed structure within the mission folder
    fold_dict = {
        "odm_dem": ("dem", False),
        "odm_orthophoto": ("orthophoto", False),
        "odm_report": ("report", False),
        "odm_texturing": ("texturing", False),
        "entwine_pointcloud": ("other", True),
        "odm_filterpoints": ("other", True),
        "odm_georeferencing": ("other", True),
        "odm_meshing": ("other", True),
        "odm_texturing_25d": ("other", True),
        "opensfm": ("other", True),
    }

    for src, (dst, containing_folder) in fold_dict.items():
        src_fold = os.path.join(task_path, src)
        dst_fold = os.path.join(mission_fold, dst)
        if client.isdir(src_fold):
            print(f"Copying to {dst_fold}")
            copy_folder(
                src_fold,
                dst_fold,
                client,
                overwrite=False,
                containing_folder=containing_folder,
            )

    # Copy files
    file_dict = {
        "all.zip": "other",
        "benchmark.txt": "other",
        "cameras.json": "other",
        "images.json": "other",
        "img_list.txt": "other",
        "log.json": "report",
        "task_output.txt": "report",
    }
    for src, dst in file_dict.items():
        src_path = os.path.join(task_path, src)
        dst_path = os.path.join(mission_fold, dst, src)
        if client.isfile(src_path):
            print(f"Copying to {dst_fold}/{src}")
            copy_file(src_path, dst_path, client, overwrite=False)

    return client.isdir(f"{mission_root}/orthophoto")

import os
from pathlib import Path

from minio import Minio
from minio.error import S3Error


def minio_login(user, password):
    """Login to MinIO Python client.

    Args
        access_key: Str. Personal access ID for MinIO. Usually a user's
                    e-mail address
        secret_key: Str. Personal secret key (i.e. password) for MinIO

    Returns
        MinIO client object.
    """
    client = Minio(
        "storage.seabee.sigma2.no",
        access_key=user,
        secret_key=password,
    )

    return client


def _jhub_path_to_minio(abs_path):
    """For files on MinIO (i.e. everything within the 'shared-seabee-ns9879k' folder
    on JuyterHub), converts an absolute file path from JupyterHub into a bucket name
    and object name (for use with the MinIO client).

    Args
        abs_path: Str. Absolute path from JupyterHub to a file or folder on MinIO
                  (i.e. within the 'shared-seabee-ns9879k' folder)

    Returns
        Tuple of strings (bucket_name, object_name).
    """
    abs_path = Path(abs_path)
    bucket_idx = abs_path.parts.index("shared-seabee-ns9879k") + 1
    bucket_name = abs_path.parts[bucket_idx]
    obj_name = "/".join(abs_path.parts[bucket_idx + 1 :])

    return (bucket_name, obj_name)


def check_minio_exists(bucket_name, obj_name, client):
    """Check whether 'obj_name' already exists on MinIO in 'bucket_name'.

    NOTE: On the SeaBee JupyterHub, it is much easier to use the 'os' module, since
    users have read access to files on MinIO. This function is only useful if you're
    using seabeepy from elsewhere.

    Args
        bucket_name: Str. Name of bucket
        obj_name:    Str. Name of object in bucket
        client:      Obj. Active MinIO Python client (from the 'minio_login' function)

    Returns
        Tuple (exists, obj_type). 'exists' is Bool (True if object exists,
        otherwise False). 'obj_type' is either 'File', 'Dir' or None.
    """
    try:
        # Check if file
        meta = client.stat_object(bucket_name, obj_name)
        exists = True
        obj_type = "File"
    except S3Error:
        # Check if folder
        objects = client.list_objects(bucket_name, prefix=obj_name, recursive=False)
        objects = [
            obj for obj in objects if (obj.object_name == f"{obj_name}/") and obj.is_dir
        ]
        if len(objects) > 0:
            exists = True
            obj_type = "Dir"
        else:
            exists = False
            obj_type = None

    return (exists, obj_type)


def copy_file_minio(src_path, dst_path, client, overwrite=False):
    """Convenience function for copying files to MinIO using absolute file paths.
    'src_path' can be anything the user had read access to; 'dst_path' must be a
    location on MinIO.

    Args
        src_path:  Str. Absolute source path
        dst_path:  Str. Absolute destination path from JupyterHub to a file on MinIO
                   (i.e. something within the 'shared-seabee-ns9879k' folder)
        client:    Obj. Active MinIO Python client (from the 'minio_login' function)
        overwrite: Bool. Default False. Whether to overwrite 'dst_path' if it already
                   exists

    Returns
        MinIO result object. Source file is copied to destination.
    """
    if os.path.isfile(dst_path) and not overwrite:
        raise OSError(
            f"File '{dst_path}' already exists. Pass 'overwrite = True' to replace."
        )

    dst_bucket, dst_name = _jhub_path_to_minio(dst_path)

    # Create dst_bucket if necessary
    dst_bucket_exists = client.bucket_exists(dst_bucket)
    if not dst_bucket_exists:
        client.make_bucket(dst_bucket)

    # Copy
    with open(src_path, "rb") as file_data:
        file_stat = os.stat(src_path)
        result = client.put_object(dst_bucket, dst_name, file_data, file_stat.st_size)

    return result


def delete_file_minio(fpath, client):
    """Delete a file on MinIo.

    Args
        fpath:  Str. Absolute path to object from JupyterHub
        client: Obj. Active MinIO Python client (from the 'minio_login' function)

    Returns
        MinIO result object
    """
    if os.path.isfile(fpath):
        bucket, name = _jhub_path_to_minio(fpath)
        result = client.remove_object(bucket, name)
    else:
        raise OSError(f"'{fpath}' is not a file.")

    return result


def delete_folder_minio(folder, client):
    """Delete a folder and all contents on MinIO. Note that if parent directory of
    'folder' only contains 'folder' (i.e. the parent will become empty after
    'folder' is removed), then the parent folder is also removed. This is just how
    S3 works.

    Args
        folder: Str. Absolute path to MinIO folder from JupyterHub
        client: Obj. Active MinIO Python client (from the 'minio_login' function)

    Returns
        None. Folder is deleted
    """
    if os.path.isdir(folder):
        bucket, name = _jhub_path_to_minio(folder)
        objects_to_delete = client.list_objects(bucket, prefix=name, recursive=True)
        for obj in objects_to_delete:
            client.remove_object(bucket, obj.object_name)
    else:
        raise OSError(f"'{folder}' is not a directory.")

    return None


def copy_folder_minio(
    src_fold, dst_fold, client, overwrite=False, containing_folder=True
):
    """Copy everything in 'src_fold' to 'dst_fold', maintaining the subfolder structure
    within 'src_fold'. 'src_fold' can be anything the user had read access to;
    'dst_fold' must be a location on MinIO (both expressed as absolute paths on the Hub).

    If 'containing_folder' is True, 'src_fold' itself will be copied into 'dst_fold'. If
    False, the contents of 'src_fold' will be copied into 'dst_fold'.

    Args
        src_fold:          Str. Absolute source path to folder on SeaBee's JupyterHub
        dst_fold:          Str. Absolute destination folder on MinIO (i.e. something
                           within the 'shared-seabee-ns9879k' folder)
        client:            Obj. Active MinIO Python client (from the 'minio_login' function)
        overwrite:         Bool. Default False. Whether to overwrite 'dst_path' if it
                           already exists
        containing_folder: Bool. Default True. If True, 'src_fold' itself will be copied
                           into 'dst_fold'; if False, the contents of 'src_fold' will be
                           copied

    Returns
        None. Folder and contents are copied.
    """
    if containing_folder:
        dst_fold = os.path.join(dst_fold, os.path.basename(src_fold))

    if os.path.isdir(dst_fold) and not overwrite:
        raise OSError(
            f"Folder '{dst_fold}' already exists. Pass 'overwrite = True' to replace."
        )

    if os.path.isdir(dst_fold) and overwrite:
        delete_folder_minio(dst_fold, client)

    src_list = Path(src_fold).rglob("*")
    src_list = [path for path in src_list if os.path.isfile(path)]
    for src_path in src_list:
        src_path = str(src_path)
        rel_path = os.path.relpath(src_path, start=src_fold)
        dst_path = os.path.join(dst_fold, rel_path)
        copy_file_minio(src_path, dst_path, client, overwrite=False)

    return None


def copy_nodeodm_results(task_id, mission_fold, client):
    """NodeODM stores its results in the 'nodeodm-workdir' on MinIO within a folder
    named according to the task's unique ID. This function copies results back to the
    mission folder. This is important as NodeODM periodically deletes everything in
    the 'nodeodm-workdir'.

    Args
        task_id:      Str. Task ID for mission in NodeODM
        mission_fold: Str. Absolute JupyterHub path to mission data.
        client:       Obj. Active MinIO Python client (from the 'minio_login' function)

    Returns
        None. Results are copied.
    """
    nodeodm_workdir = r"/home/notebook/shared-seabee-ns9879k/nodeodm-workdir"
    res_fold = os.path.join(nodeodm_workdir, task_id)

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
        src_fold = os.path.join(res_fold, src)
        dst_fold = os.path.join(mission_fold, dst)
        if os.path.isdir(src_fold):
            copy_folder_minio(
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
        src_path = os.path.join(res_fold, src)
        dst_path = os.path.join(mission_fold, dst, src)
        if os.path.isfile(src_path):
            copy_file_minio(src_path, dst_path, client, overwrite=False)

    return None
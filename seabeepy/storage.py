import os
from pathlib import Path

from minio import Minio
from minio.commonconfig import CopySource
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


def _check_minio_exists(bucket_name, obj_name, client):
    """Check whether 'obj_name' already exists on MinIO in 'bucket_name'.

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
    """Convenience function for copying files to MinIO using absolute file paths from
    JupyterHub. 'src_path' can either be a local path or an existing file on MinIO;
    'dst_path' must be a location on MinIO.

    Args
        src_path:  Str. Absolute source path on SeaBee's JupyterHub
        dst_path:  Str. Absolute destination path from JupyterHub to a file on MinIO
                   (i.e. something within the 'shared-seabee-ns9879k' folder)
        client:    Obj. Active MinIO Python client (from the 'minio_login' function)
        overwrite: Bool. Default False. Whether to overwrite 'dst_path' if it already
                   exists

    Returns
        MinIO result object. Source file is copied to destination.
    """
    if "shared-seabee-ns9879k" in src_path:
        src_minio = True
        src_bucket, src_name = _jhub_path_to_minio(src_path)
    else:
        src_minio = False

    dst_bucket, dst_name = _jhub_path_to_minio(dst_path)
    dst_exists, dst_type = _check_minio_exists(dst_bucket, dst_name, client)
    if dst_exists and not overwrite:
        raise OSError(
            f"File '{dst_path}' already exists on MinIO. Pass 'overwrite = True' to replace."
        )

    # Create dst_bucket if necessary
    dst_bucket_exists = client.bucket_exists(dst_bucket)
    if not dst_bucket_exists:
        client.make_bucket(dst_bucket)

    # Copy
    if src_minio:
        result = client.copy_object(
            dst_bucket,
            dst_name,
            CopySource(src_bucket, src_name),
        )
    else:
        with open(src_path, "rb") as file_data:
            file_stat = os.stat(src_path)
            result = client.put_object(
                dst_bucket, dst_name, file_data, file_stat.st_size
            )

    return result


def delete_file_minio(fpath, client):
    """Delete a file on MinIo.

    Args
        fpath:  Str. Absolute path to object from JupyterHub
        client: Obj. Active MinIO Python client (from the 'minio_login' function)

    Returns
        MinIO result object
    """
    bucket, name = _jhub_path_to_minio(fpath)
    exists, obj_type = _check_minio_exists(bucket, name, client)

    if exists and (obj_type == "File"):
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
    bucket, name = _jhub_path_to_minio(folder)
    exists, obj_type = _check_minio_exists(bucket, name, client)

    if exists and (obj_type == "Dir"):
        objects_to_delete = client.list_objects(bucket, prefix=name, recursive=True)
        for obj in objects_to_delete:
            result = client.remove_object(bucket, obj.object_name)
    else:
        raise OSError(f"'{folder}' is not a directory.")

    return None


def copy_folder_minio(
    src_fold, dst_fold, client, overwrite=False, containing_folder=True
):
    """Copy everything in 'src_fold' to 'dst_fold', maintaining the subfolder structure
    within 'src_fold'. 'src_fold' can either be on MinIO or a 'local' path on the SeaBee
    JupyterHub; 'dst_fold' must be a location on MinIO (both expressed as absolute paths
    on the Hub).

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
    dst_bucket, dst_name = _jhub_path_to_minio(dst_fold)
    dst_exists, dst_type = _check_minio_exists(dst_bucket, dst_name, client)

    if dst_exists and not overwrite:
        raise OSError(
            f"Folder '{dst_fold}' already exists on MinIO. Pass 'overwrite = True' to replace."
        )

    if dst_exists and overwrite:
        delete_folder_minio(dst_fold, client)

    src_list = Path(src_fold).rglob("*")
    src_list = [path for path in src_list if os.path.isfile(path)]
    for src_path in src_list:
        src_path = str(src_path)
        rel_path = os.path.relpath(src_path, start=src_fold)
        dst_path = os.path.join(dst_fold, rel_path)
        print(src_path, dst_path)
        result = copy_file_minio(src_path, dst_path, client, overwrite=False)

    return None
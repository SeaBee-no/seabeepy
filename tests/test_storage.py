import pytest

import seabeepy as sb


def test_jhub_path_to_minio_none():

    bucket, object_path = sb.storage._jhub_path_to_minio("/home/notebook/cogs/")

    assert bucket is None
    assert object_path is None


def test_jhub_path_to_minio_shared():

    bucket, object_path = sb.storage._jhub_path_to_minio("/home/notebook/shared-seabee-ns9879k/bucket/object")

    assert bucket=="bucket"
    assert object_path == "object"


def test_jhub_path_to_minio_s3():

    bucket, object_path = sb.storage._jhub_path_to_minio("bucket/object/filename")

    assert bucket=="bucket"
    assert object_path == "object/filename"
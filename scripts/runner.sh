#!/bin/bash

mc alias set seabee-minio https://storage.seabee.sigma2.no $MINIO_ACCESS_ID $MINIO_SECRET_KEY
jupyter nbconvert --execute  --allow-errors --to notebook --inplace ./seabirds_runner.ipynb
mc cp ./seabirds_runner.ipynb seabee-minio/notebook-logs/seabirds_runner-$( date '+%H' ).ipynb
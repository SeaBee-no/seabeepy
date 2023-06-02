#!/bin/bash
echo "Flight take-off"
mc alias set seabee-minio https://storage.seabee.sigma2.no $MINIO_ACCESS_ID $MINIO_SECRET_KEY
jupyter nbconvert --execute  --allow-errors --to notebook --inplace ./flights_runner.ipynb
mc cp ./flights_runner.ipynb seabee-minio/notebook-logs/flights_runner-$( date '+%H' ).ipynb
echo "Flight landing"

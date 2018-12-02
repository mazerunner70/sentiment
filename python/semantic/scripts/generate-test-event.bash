#!/bin/bash

. ~/.env

sam local generate-event s3 put --bucket ${STAGING_S3} --key test1.csv | sam local invoke --debug CreateThumbnail

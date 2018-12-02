#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
echo "This script located at ${SCRIPT_DIR}"

RELATIVE_DIR="../sam-app"
SAM_APP_DIR="$( cd ${SCRIPT_DIR}/${RELATIVE_DIR} >/dev/null && pwd )"
if [ ! -d "$SAM_APP_DIR" ]; then
    printf "Error - ${SAM_APP_DIR} should be a valid dir!\n"
    exit 3
fi

printf "SAM app directory at ${SAM_APP_DIR}\n"

pushd ${SAM_APP_DIR}

#create zip file
cd build
rm ../updated-lambda.zip
zip -r ../updated-lambda.zip *
cd ..

#Upload to AWS
aws lambda update-function-code --function-name wils-semantic-1-CreateThumbnail-1P2UYV495YR92 --zip-file fileb://updated-lambda.zip
rm updated-lambda.zip
popd

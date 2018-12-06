#!/bin/bash

. ~/.env



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

aws s3 cp access-swagger.yaml s3://wils-staging

sam deploy \
   --template-file /tmp/packaged.yaml \
   --stack-name semantic-1 \
   --capabilities CAPABILITY_IAM \
   --region eu-west-2


popd

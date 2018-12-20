#!/bin/bash

. ~/.env

STACK_NAME="semantic-3"

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

aws s3 cp access-swagger.yaml s3://${STAGING_S3}

sam deploy \
   --template-file /tmp/packaged.yaml \
   --stack-name ${STACK_NAME} \
   --capabilities CAPABILITY_IAM \
   --region eu-west-1


popd

API_ID=`aws cloudformation describe-stacks --stack ${STACK_NAME} --region ${REGION} --query "Stacks[].Outputs[?OutputKey=='ApiId'].OutputValue" --output text`
API_URL=`aws cloudformation describe-stacks --stack ${STACK_NAME} --region ${REGION} --query "Stacks[].Outputs[?OutputKey=='ApiUrl'].OutputValue" --output text`
UPLOAD_BUCKET=`aws cloudformation describe-stacks --stack ${STACK_NAME} --region ${REGION} --query "Stacks[].Outputs[?OutputKey=='UploadBucket'].OutputValue" --output text`
COGNITO_USER_POOL_ID=`aws cloudformation describe-stacks --stack ${STACK_NAME} --region ${REGION} --query "Stacks[].Outputs[?OutputKey=='CognitoUserPoolId'].OutputValue" --output text`
COGNITO_USER_POOL_CLIENT_ID=`aws cloudformation describe-stacks --stack ${STACK_NAME} --region ${REGION} --query "Stacks[].Outputs[?OutputKey=='CognitoUserPoolClientId'].OutputValue" --output text`

printf "API_ID: ${API_ID}\n"
printf "API_URL: ${API_URL}\n"
printf "UPLOAD_BUCKET: ${UPLOAD_BUCKET}\n"
printf "COGNITO_USER_POOL_ID: ${COGNITO_USER_POOL_ID}\n"
printf "COGNITO_USER_POOL_CLIENT_ID: ${COGNITO_USER_POOL_CLIENT_ID}\n"


#!/bin/bash

pushd ../../../python/lambda
zip ../../aws/tmp/HelloWorld.zip hello-world.py
cd ../aws

aws lambda create-function \
  --function-name HelloWorld \
  --zip-file fileb://tmp/HelloWorld.zip \
  --handler hello-world.lambda_handler \
  --runtime python2.7 \
  --role arn:aws:iam::915524423834:role/lambda-s3-role \
  --timeout 10 \
  --memory-size 1024

popd

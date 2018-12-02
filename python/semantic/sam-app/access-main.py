import boto3
import json
import os
from os.path import join, dirname 
from dotenv import load_dotenv

#from access.access import Access

# https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
def lambda_handler(event, context):
    print('hello')
    print('Event: ', event)
    print('httpMethod', event['httpMethod'])
    print('resource', event['resource'])
    dotenv_path = join(os.getcwd(), '.env')
#        print (dotenv_path)
    load_dotenv(dotenv_path)
#
    print('111', os.environ['S3_BUCKET'])

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(os.environ['S3_BUCKET'][13:])

    print('233', [file.key for file in bucket.objects.all()])


#    call(['printenv'])

#    access = Access()
#    resultDict = access.process(event['httpMethod'], event['resource'])
    resultDict = {'dummy':1}
    print (resultDict)

    resultBody = json.dumps(resultDict)

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": { "Content-Type": "application/json"},
        "body": resultBody
    }

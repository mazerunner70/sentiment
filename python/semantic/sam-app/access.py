import boto3
#from  semantic.semantic import Semantic

# https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
def lambda_handler(event, context):
    print('hello')
    print('Event: ', event)

#    call(['printenv'])


    return {
    "isBase64Encoded": False,
    "statusCode": 200,
    "headers": { "Content-Type": "application/json"},
    "body": "All worked"
}

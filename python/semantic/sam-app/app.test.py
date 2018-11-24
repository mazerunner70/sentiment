import boto3


def lambda_handler(event, context):
    print('hello')
    print('Event: ', event)
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    print(s3_client.list_buckets())
    bucket = s3.Bucket('sam-app-2-semanticwils-1abkdu7pxckbs')
    print ([file.key for file in bucket.objects.all()])
    print('---')



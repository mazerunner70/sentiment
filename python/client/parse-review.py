import boto3

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

#Upload a new file
data = open('file1.jpg', 'rb')
s3.Bucket('semantic-wils').put_object(Key='test.jpg', Body=data)
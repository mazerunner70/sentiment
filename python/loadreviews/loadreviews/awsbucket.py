import boto3
import os
import sys
import json
from os.path import join, dirname 
from dotenv import load_dotenv

class AwsBucket():
    def __init__(self):
        s3 = boto3.resource('s3')
        dotenv_path = join(os.getcwd(), '.env')
#        print (dotenv_path)
        load_dotenv(dotenv_path)
#        print (os.getenv('jpw'))
        bucketname = str(os.getenv('S3_BUCKET'))
        self.bucket = s3.Bucket(bucketname)

    def getFileList(self):
#        print (list(bucket.objects.all()))
#        for file in self.bucket.objects.all():
#            print (file.key)
        return [file.key for file in self.bucket.objects.all()]

    def upload(self, filename):
        data = open('/tmp/'+filename, 'rb')
        self.bucket.put_object(Key=filename, Body=data)

if __name__ == '__main__':
    print ('Starting awsBucket')
    awsbucket = AwsBucket()
    awsbucket.getFileList()

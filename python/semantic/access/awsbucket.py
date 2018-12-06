import boto3
import os
from os.path import join, dirname 
from dotenv import load_dotenv

class AwsBucket():
    def __init__(self):
        dotenv_path = join(os.getcwd(), '.env')
        print(dotenv_path)
        load_dotenv(dotenv_path)
        print('111', os.environ['S3_BUCKET'])
        s3 = boto3.resource('s3')
        self.bucket = s3.Bucket(os.environ['S3_BUCKET'])


    def getFileList(self):
        return [file.key for file in self.bucket.objects.all()]

    def upload(self, local_filename,s3_filename):
        data = open(local_filename, 'rb')
        self.bucket.put_object(Key=s3_filename, Body=data)

    def download(self, s3_filename, local_filename):
        self.bucket.download_file(Key=s3_filename, Filename=local_filename)


if __name__ == '__main__':
    print ('Starting awsBucket')
    awsbucket = AwsBucket()
    print(awsbucket.getFileList())

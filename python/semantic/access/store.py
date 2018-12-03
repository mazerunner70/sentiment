import boto3
import os
from os.path import join, dirname 
from dotenv import load_dotenv


class Store:
    def __init__(self):
        dotenv_path = join(os.getcwd(), '.env')
        load_dotenv(dotenv_path)
        print('111', os.environ['S3_BUCKET'])
        s3 = boto3.resource('s3')
        self.bucket = s3.Bucket(os.environ['S3_BUCKET'][13:])

    def get_sortedfilelist(self):
        filelist = [file.key for file in self.bucket.objects.all()]
        return sorted(filelist)



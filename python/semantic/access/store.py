import boto3
import os
import csv
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

    def loadcsv(self, filename):
        local_filename = self.movefiletolocal(filename)
        return self.read_local_csv(local_filename)

    def movefiletolocal(self, filename):
        local_filename = '/tmp/{}'.format(os.path.basename(filename))
        self.bucket.download_file(filename, local_filename)
        return local_filename

    def read_local_csv(self, local_filename):
        csv_list = []
        with open(local_filename, "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                csv_list.append(row)
        return csv_list

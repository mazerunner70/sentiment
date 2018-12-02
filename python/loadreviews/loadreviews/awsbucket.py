#!/usr/bin/env python3

import boto3

class AwsBucket():
    def __init__(self):
        s3 = boto3.resource('s3')
        self.bucket = s3.Bucket('wils-semantic-1-semanticwils-nvdo5aw1g8lf')

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

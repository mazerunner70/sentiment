import boto3
import sys
import imp
from comprehend.comprehend import Comprehend

def lambda_handler(event, context):
    print('hello')
    print('Event: ', event)

#    call(['printenv'])
    comprehend = Comprehend()
    comprehend.execute()

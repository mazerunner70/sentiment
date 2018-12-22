import boto3
import sys
import imp
from subprocess import call
sys.modules['sqlite-dev'] = imp.new_module('sqlite-dev')
sys.modules['sqlite3.dbapi2'] = imp.new_module('sqlite3.dbapi2')
from comprehend.comprehend import Comprehend

def lambda_handler(event, context):
    print('hello')
    print('Event: ', event)

#    call(['printenv'])
    comprehend = Comprehend()
    comprehend.execute()

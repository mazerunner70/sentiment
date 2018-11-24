import os
import json
from os.path import join, dirname 
from dotenv import load_dotenv
import requests

dotenv_path = join(os.getcwd(), 'dev.env1')
print (dotenv_path)
load_dotenv(dotenv_path)
print (os.getenv('jpw'))
jpw = str(os.getenv('jpw'))+'1'
print(jpw)
startAt=0
url='https://jira.bgchtest.info/rest/api/2/search?startAt='+str(startAt)+'&fields=Key,description,created&expand=description&jql=project=RNTIR'
print (url)
response = requests.get(url, auth=("william.o'hara@hivehome.com", jpw))
#print(response.text)

with open('jira-response.json', 'w') as text_file:
    text_file.write(response.text)

print('Parsing response')
json_data = json.loads(response.text)
print ('issues', len(json_data))
print ('startAt', json_data["startAt"])
issues = json_data['issues']
print( 'issues:', len(issues))
#print issues[0]
print('Total:', json_data["total"])



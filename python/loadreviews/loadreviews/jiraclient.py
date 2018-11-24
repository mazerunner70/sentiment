import requests
import unicodedata
import os
import json
from os.path import join, dirname 
from dotenv import load_dotenv

class JiraClient():
    def getSummary(self, description):
#        print('210', description)
        startPos = description.find('{color:navy}')
        endPos = description.find('{color}')
        #print 'dd',startPos, endPos
        if (startPos>-1):
            subString = description[startPos+12:endPos]
            return subString
        return '<wils-crash-marker>'

    def normaliseUnicode(self, unicodeString):
        return unicodedata.normalize('NFKD', unicodeString).encode('ascii','ignore')

    def getChunk(self, startAt):
        dotenv_path = join(os.getcwd(), '.env')
#        print (dotenv_path)
        load_dotenv(dotenv_path)
#        print (os.getenv('jpw'))
        jpw = str(os.getenv('jpw'))+'1'
        url='https://jira.bgchtest.info/rest/api/2/search?startAt='+str(startAt)+'&fields=Key,description,created&expand=description&jql=project=RNTIR'
        response = requests.get(url, auth=("william.o'hara@hivehome.com",jpw))
#        print ('111',response)
        json_data = response.json()
#        json_data = json.loads(response.text)
#        print ('222',json_data)
        issues = json_data['issues']
        total = json_data["total"]
        summaries = []
        for issue in issues:
            description = issue["fields"]["description"]
            created = issue["fields"]["created"]
            key = issue["key"]
            summary = self.getSummary(description)
            summaries.append({'key': key, 'created': created, 'summary': summary})
        return {'total': total, 'summaries': summaries}


if __name__ == '__main__':
    jiraclient = JiraClient()
    jiraclient.getChunk(0)
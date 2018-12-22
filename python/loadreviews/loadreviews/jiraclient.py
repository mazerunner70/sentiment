import requests
import unicodedata
import os
import sys
import json
from os.path import join, dirname 
from dotenv import load_dotenv

class JiraClient():
    def __init__(self, issueKey):
        self.issueKey = issueKey

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
        
        url = str(os.getenv('JIRA_URL'))
        username= str(os.getenv('username'))
        rangeClause =  ' and key > "RNTIR-'+str(self.issueKey)+'"' if self.issueKey >0 else ''
        url=url+'rest/api/2/search?startAt='+str(startAt)+'&fields=Key,description,created&expand=description&jql=project=RNTIR'+rangeClause
        print (url)
        response = requests.get(url, auth=(username,jpw))
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
    jiraclient = JiraClient(2)
    jiraclient.getChunk(0)
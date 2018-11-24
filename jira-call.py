#!/usr/bin/env python

import requests
import json
import csv
import unicodedata

def getSummary(description):
    startPos = description.find('{color:navy}')
    endPos = description.find('{color}')
    #print 'dd',startPos, endPos
    if (startPos>-1):
        subString = description[startPos+12:endPos]
        return subString
    return '<wils-crash-marker>'

def saveCsvToFile(fileName, csvToSave):
    with open(fileName, "w") as csvFile:
        lineWriter = csv.writer(csvFile)
        for row in csvToSave:
            lineWriter.writerow(row)
    csvFile.close()


#r = requests.get('https://jira.bgchtest.info/rest/api/latest/issue/RNTIR-1209', auth=("william.o'hara@hivehome.com", ''))
#print(r.text)
outputList = []
total = 50
ctr = 0
def getChunk(startAt):
    url='https://jira.bgchtest.info/rest/api/2/search?startAt='+str(startAt)+'&fields=Key,description,created&expand=description&jql=project=RNTIR'
    print url
    response = requests.get(url, auth=("william.o'hara@hivehome.com", ''))
    #print(response.text)
    json_data = json.loads(response.text)
    #print 'issues', len(json_data)
    #print '22', json_data["startAt"]
    issues = json_data['issues']
    #print 'issues:', len(issues)
    #print issues[0]
    total = json_data["total"]
    for issue in issues:
        description = issue["fields"]["description"]
        createdUnicode = issue["fields"]["created"]
        #print issue["key"], getSummary(description)
        key = unicodedata.normalize('NFKD', issue["key"]).encode('ascii','ignore')
        summaryUnicode = getSummary(description)
        summary = summaryUnicode if summaryUnicode == '<wils-crash-marker>'  else unicodedata.normalize('NFKD', summaryUnicode).encode('ascii','ignore')
        created = unicodedata.normalize('NFKD', createdUnicode).encode('ascii','ignore')
        outputList.append([key, created, summary])
    return total

while (ctr<total):
    total = getChunk(ctr)
    print ctr, total
    ctr = ctr+50

saveCsvToFile('file.csv', outputList)


#r = requests.get('https://jira.bgchtest.info/rest/api/2/issue/createmeta?projectKeys=RNTIR', auth=("william.o'hara@hivehome.com", 'L1ll1aN01'))
#print(r.text)



#!/usr/bin/env python

from textblob import TextBlob
import csv
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
from datetime import datetime

tb = Blobber(analyzer=NaiveBayesAnalyzer())

def loadCsvIntoMemory(fileName):
    rows = []
    with open(fileName, "r") as csvFile:
        lineReader = csv.reader(csvFile)
        for row in lineReader:
            rows.append(row)
    csvFile.close()
    return rows    

def saveListToFile(filename, listToSave):
    with open(filename, "w") as textFile:
        for row in listToSave:
            textFile.write("%s\n" % row)
    textFile.close()

def saveCsvToFile(fileName, csvToSave):
    with open(fileName, "w") as csvFile:
        lineWriter = csv.writer(csvFile)
        for row in csvToSave:
            lineWriter.writerow(row)
    csvFile.close()


sourceListName = 'file.csv'
sourceList = loadCsvIntoMemory(sourceListName)
print "Count of rows ", len(sourceList)
print "row 2 ", sourceList[2][1]
summaries = list(map(lambda row: row[2], sourceList))
summary = ' '.join(summaries)
#print summary
summaryBlob = TextBlob(summary)
words = summaryBlob.words
print 'words:', len(words)

saveListToFile('interim/wordlist.txt', words)
uniqueWords = set(map(lambda row: row.lower(), words))
print "unique: ", len(uniqueWords)
saveListToFile('interim/unique-wordlist.txt', uniqueWords)
frequencyList = []
for word in uniqueWords:
    frequencyList.append([summaryBlob.word_counts[word], word])
newList = sorted(frequencyList, key=lambda row: row[0])
newList.reverse()
#print '888', newList
saveCsvToFile('interim/word-freq.csv', newList)

#opinion = TextBlob("EliteDataScience.com is dope.")
#print "he"
#print opinion.sentiment

#monty = TextBlob("We are no longer the Knights who say Ni. "
 #                    "We are now the Knights who say Ekki ekki ekki PTANG.")
#print monty.word_counts['ekki']

dateObject = datetime.strptime(sourceList[2][1][0:10], '%Y-%m-%d')
print dateObject.strftime('%Y-%m-%d')
val = tb("happy sentence you gladly want to test").sentiment
print val, val.classification
val = TextBlob("happy sentence you gladly want to test").sentiment
print val, val.polarity

dailyReports = {}
for feedback in sourceList:
    dateObject = datetime.strptime(feedback[1][0:10], '%Y-%m-%d')
    dayReport = dailyReports.setdefault(dateObject.strftime('%Y-%m-%d'), [])
    dayReport.append(TextBlob(feedback[2]).sentiment.polarity)

outputDates = []
for key in dailyReports.keys():
    outputDates.append( [key, sum(dailyReports[key])/len(dailyReports[key])] )
sortedOutputDates = sorted(outputDates, key=lambda row: row[0])

saveCsvToFile('interim/sentiment.csv', sortedOutputDates)


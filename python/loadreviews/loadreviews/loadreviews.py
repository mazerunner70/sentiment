#!/usr/bin/env python3

from loadreviews.store import Store
from loadreviews.issueiterator import IssueIterator
from loadreviews.csvutils import saveList

class LoadReviews(object):
    def __init__(self):
        self.store = Store()

    def execute(self):
        store = Store()
        processedRecords = store.getIssuesRangeProcessed()
        if processedRecords.upper > 0:
            print ('found uploaded records, up to RNTIR-', processedRecords.upper)
        else:
            print ('Starting upload from scratch')
        next_record = processedRecords.upper+1
        issues = self.loadNewIssues(next_record)
        if (issues):
            print ('Found ', len(issues), ' to load')
            fileName = saveList(issues)
            self.uploadToS3(fileName)
        else:
            print ('No new records found')

    def loadNewIssues(self, next_record):
        issue_iterator = IssueIterator(next_record)
        issues = []
        for issue in issue_iterator:
            issues.append(issue)
        return issues
        
    def uploadToS3(self,filename):
        print('Uploading from ', filename)
        self.store.uploadToBucket(filename)

if __name__ == '__main__':
    print ('Starting')
    load_reviews = LoadReviews()
    load_reviews.execute()
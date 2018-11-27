import collections
from loadreviews.awsbucket import AwsBucket
import re

class Store:
    def __init__(self):
        self.awsbucket = AwsBucket()
        self.s3_files = self.awsbucket.getFileList()
    
    def getReportFileList(self):
        pattern = re.compile(r"records-RNTIR-(\d*)-RNTIR-(\d*)\.")
        return list(filter(lambda file: pattern.match(file), self.s3_files))

    def getReportRange(self):
        filenames = self.getReportFileList()
        pattern = re.compile(r'records-RNTIR-(\d*)-RNTIR-(\d*)\.')
        lowest = 100000
        highest = 0
        for filename in filenames:
            match = pattern.match(filename)
            highest = max(int(match.group(2)),highest)
            lowest = min(int(match.group(1)), lowest)
        return range(lowest, highest)
       
    def uploadToBucket(self, filename):
        self.awsbucket.upload(filename)

    def getLastEntry(self, filenames):
        pattern = re.compile(R'records-RNTIR-(\d*)-RNTIR-(\d*)\.')
        lowest = 100000
        highest = 0
        for filename in filenames:
            match = pattern.match(filename)
#            print (filename, match)
#            print (match.groups())
            highest = max(int(match.group(2)),highest)
            lowest = min(int(match.group(1)), lowest)
        return range(lowest, highest)

if __name__ == '__main__':
    print ('Starting')
    store = Store()
    range = store.getReportRange()
    print (range.lower)

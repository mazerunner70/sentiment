import collections
from loadreviews.awsbucket import AwsBucket
import re

ProcessedRange = collections.namedtuple('ProcessedRange', 'lower upper' )


class Store:
    def __init__(self):
        self.awsBucket = AwsBucket()
    
    def getIssuesRangeProcessed(self):
        fileList = self.awsBucket.getFileList()
        filenames = list(filter(lambda filename: filename.startswith('records '), fileList))
        last_entry = self.getLastEntry(filenames)
        return last_entry

    def uploadToBucket(self, filename):
        self.awsBucket.upload(filename)

    def getLastEntry(self, filenames):
        pattern = re.compile('records RNTIR-(\\d*)-RNTIR-(\\d*)')
        lowest = 100000
        highest = 0
        for filename in filenames:
            match = pattern.match(filename)
#            print (filename, match)
#            print (match.groups())
            highest = max(int(match.group(2)),highest)
            lowest = min(int(match.group(1)), lowest)
        return ProcessedRange(lowest, highest)

if __name__ == '__main__':
    print ('Starting')
    store = Store()
    range = store.getIssuesRangeProcessed()
    print (range.lower)

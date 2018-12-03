from semantic.store import Store

class ReportIterator:
    def __init__(self, s3_files_to_do):
        self.store = Store()
        self.batch_ctr = 0
        self.batch = []    
        self.s3_files_to_do = s3_files_to_do

    def __iter__(self):
        return self

    def __next__(self):
        if self.batch_ctr == len(self.batch):
            self.nextBatch()
        if self.batch_ctr < len(self.batch):
            return self.getNextEntry()
        raise StopIteration()
    
    def nextBatch(self):
        filename = self.s3_files_to_do and self.s3_files_to_do.pop()
        if filename:
            self.readBatch(filename)
        else:
            raise StopIteration()

    def readBatch(self, filename):
        local_filename = self.store.moveFileToLocal(filename)
        self.batch = self.store.read_local_csv(local_filename)
        self.batch_ctr = 0

    def getNextEntry(self):
        result = self.batch[self.batch_ctr]
        self.batch_ctr += 1
        return result


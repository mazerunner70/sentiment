import re

from access.store import Store

class ReportIterator:
    def __init__(self, start_number):
        self.store = Store()
        self.reportid = start_number
        self.batch = []
        self.sorted_filelist = self.store.get_sortedfilelist()
        self.filelist_index = 0


    def __iter__(self):
        return self

    def __next__(self):
        if len(self.batch)==0:
            self.load_newbatch()
        report = self.batch.pop()
        return report

    def load_newbatch(self):
        if len(self.sorted_filelist) == self.filelist_index:
            raise StopIteration()
        filename = self.sorted_filelist[self.filelist_index]
        self.filelist_index += 1
        pattern = re.compile(r"records-RNTIR-(\d*)-RNTIR-(\d*)-processed")
        match = pattern.match(filename)
        if not match:
            self.load_newbatch()
            return
        higher = match.group(2)
        if int(higher) < self.reportid:
            self.load_newbatch()
            return
        self.batch = self.store.loadcsv(filename)
        if len(self.batch) == 0:
            self.load_newbatch()
            return
            


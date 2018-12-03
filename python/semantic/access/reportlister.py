import re
from access.store import Store

class ReportLister:
    def __init__(self):
        self.store = Store()

    def getrange(self):
        filelist = self.store.get_sortedfilelist()
        print ()
        processed_filelist = self.get_processedfilelist(filelist)
        return self.getfilerange(processed_filelist)

    def get_processedfilelist(self, filelist):
        pattern = re.compile(r"records-RNTIR-(\d*)-RNTIR-(\d*)-processed")
        return list(filter(lambda file: pattern.match(file), filelist))

    def getfilerange(self, processedfilelist):
        pattern = re.compile(r"records-RNTIR-(\d*)-RNTIR-(\d*)-processed")
        lowest, highest = 10000, 0
        for processedfile in processedfilelist:
            match = pattern.match(processedfile)
            highest = max(int(match.group(2)),highest)
            lowest = min(int(match.group(1)), lowest)
        return {"lowest": lowest, "highest": highest}

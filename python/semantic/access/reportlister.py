import re
from access.store import Store
from access.report_iterator import ReportIterator

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

    def getreports(self, report_range, index, pagesize):
        print('getting reports between', report_range.start, ' and ', report_range.stop, ' with index ', index,' and pagesize',pagesize)
        report_iterator = ReportIterator(report_range.start)
        report = 0
        while True:
            report = next(report_iterator)
            id = int(report[0][6:])
            if id >=report_range.start:
                break
        for f in range(0,index):
            report = next(report_iterator)
        reports = []
        try:
            while True:
                id = int(report[0][6:])
                if id > report_range.stop:
                    break
                reports.append(report)
                if len(reports) == pagesize:
                    break
                report = next(report_iterator)
        except StopIteration:
            pass # allow that valid end of the available records
        return reports
       
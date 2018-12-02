

from access.reportlister import ReportLister

class Access:
    def __init__(self):
        pass

    def process(self, httpMethod, resource):
        if httpMethod == 'GET':
            self.processGet(resource)
        return { 'Error', 'Method not supported'}
    
    def processGet(self, resource):
        if resource == '/reports':
            self.getReportList()

    def getReportList(self):
        reportLister = ReportLister()
        return reportLister.getRange()

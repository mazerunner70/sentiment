

from access.reportlister import ReportLister

class Access:
    def __init__(self):
        pass

    def process(self, httpMethod, resource):
        if httpMethod == 'GET':
            return self.processGet(resource)
        return { 'Error', 'Method not supported'}
    
    def processGet(self, resource):
        if resource == '/reports':
            return self.getReportList()
        return { 'Error', 'resource not supported'}

    def getReportList(self):
        reportLister = ReportLister()
        return reportLister.getrange()

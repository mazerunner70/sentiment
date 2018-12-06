

from access.reportlister import ReportLister

class Access:

    def process(self, httpMethod, resource, parameters):
        if httpMethod == 'GET':
            return self.processGet(resource, parameters)
        return { 'Error', 'Method not supported'}
    
    def processGet(self, resource, parameters):
        if resource == '/reports':
            return self.getreportlist()
        if resource == '/report':
            return self.getreport_range(parameters)
        return { 'Error', 'resource not supported'}

    def getreportlist(self):
        reportLister = ReportLister()
        return reportLister.getrange()

    def getreport_range(self, parameters):
        reportlister = ReportLister()
        report_range = self.asrange(parameters.get('range'))
        index = parameters.get('index', 0)
        pagesize = parameters.get('pagesize', -1)
        return reportlister.getreports(report_range, index, pagesize)

    def asrange(self, rangestring):
        print(222, rangestring)
        rangelist = rangestring.split('-')
        if len(rangelist[1]) == 0:
            rangelist[1] = '100000'
        return range(int(rangelist[0]), int(rangelist[1]))
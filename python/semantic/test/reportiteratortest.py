import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from semantic.reportiterator import ReportIterator

class TestReportIterator(unittest.TestCase):
    @patch('semantic.reportiterator.Store')
    def testNoFiles(self, mockClass):
        reportIterator = ReportIterator([])
        ctr = 0
        for report in reportIterator:
            ctr +=1
        self.assertEqual(0, ctr)

    @patch('semantic.reportiterator.Store')
    def testOneFile(self, mockClass):
        mockClass.return_value.moveFileToLocal.return_value = 'local:File'
        mockClass.return_value.readLocalCsv.return_value = [[1, '12', '34']]
        reportIterator = ReportIterator([
            'records RNTIR-00002-RNTIR-00002.csv'
        ])
        ctr = 0
        resultList = []
        for report in reportIterator:
            ctr +=1
            resultList.append(report)
        self.assertEqual(1, ctr)
        self.assertEqual([[1, '12', '34']], resultList)

    @patch('semantic.reportiterator.Store')
    def testTwoFiles(self, mockClass):
        mockClass.return_value.moveFileToLocal.return_value = 'local:File'
        mockClass.return_value.readLocalCsv.return_value = [[1, '12', '34']]
        reportIterator = ReportIterator([
            'records RNTIR-00002-RNTIR-00002.csv',
            'records RNTIR-00002-RNTIR-00002.csv'
        ])
        ctr = 0
        resultList = []
        for report in reportIterator:
            ctr +=1
            resultList.append(report)
        self.assertEqual(2, ctr)
        self.assertEqual([[1, '12', '34'], [1, '12', '34']], resultList)

if __name__ == '__main__':
    unittest.main()


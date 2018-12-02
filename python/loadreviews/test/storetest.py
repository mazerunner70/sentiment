import unittest
from unittest.mock import MagicMock, PropertyMock, patch
from loadreviews.store import Store


class TestStore(unittest.TestCase):

    @patch('loadreviews.store.AwsBucket')
    def testFileLists(self, mockClass):
        mockClass.return_value.getFileList.return_value = [
            'records-RNTIR-01644-RNTIR-01647-processed.csv', 
            'records-RNTIR-01644-RNTIR-01647.csv', 
            'records-RNTIR-01644-RNTIR-01648.csv'
        ]
        store = Store()
        self.assertEqual([
            'records-RNTIR-01644-RNTIR-01647.csv',
            'records-RNTIR-01644-RNTIR-01648.csv'
        ], store.getReportFileList())

    @patch('loadreviews.store.AwsBucket')
    def testReportRange(self, mockClass):
        mockClass.return_value.getFileList.return_value = [
            'records-RNTIR-01644-RNTIR-01647.csv', 
            'records-RNTIR-01640-RNTIR-01643.csv'
        ]
        store = Store()
        reportRange = store.getReportRange()
        self.assertEqual(1640, reportRange.start)
        self.assertEqual(1647, reportRange.stop)
        

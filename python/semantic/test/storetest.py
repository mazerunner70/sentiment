import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from semantic.store import Store


class TestStore(unittest.TestCase):
    @patch('semantic.store.AwsBucket')
    def testNoFileInDir(self, mockClass):
        mockClass.return_value.getFileList.return_value = [
        ]
        store = Store()
        self.assertEqual(store.getReportFileList(), [
        ])

    @patch('semantic.store.AwsBucket')
    def testNoUsefulFileInDir(self, mockClass):
        mockClass.return_value.getFileList.return_value = [
            'useless.js'
        ]
        store = Store()
        self.assertEqual(store.getReportFileList(), [
        ])

    @patch('semantic.store.AwsBucket')
    def testOneFileInDir(self, mockClass):
        mockClass.return_value.getFileList.return_value = [
            'records RNTIR-00002-RNTIR-01647.js'
        ]
        store = Store()
        self.assertEqual(store.getReportFileList(), [
            'records RNTIR-00002-RNTIR-01647.js'
        ])

    @patch('semantic.store.AwsBucket')
    def testOneFileInDir(self, mockClass):
        mockClass.return_value.getFileList.return_value = [
            'records RNTIR-00002-RNTIR-01647.js',
            'records RNTIR-00002-RNTIR-01647 processed.js'
        ]
        store = Store()
        self.assertEqual(store.getReportFileList(), [
            'records RNTIR-00002-RNTIR-01647.js'
        ])
        self.assertEqual(store.getProcessedFileList(), [
            'records RNTIR-00002-RNTIR-01647 processed.js'
        ])

    @patch('semantic.store.AwsBucket')
    def testOneUsefulFileInDir(self, mockClass):
        mockClass.return_value.getFileList.return_value = [
            'records RNTIR-00002-RNTIR-01647.js',
            'useless.js'
        ]
        store = Store()
        self.assertEqual(store.getReportFileList(), [
            'records RNTIR-00002-RNTIR-01647.js'
        ])


    @patch('semantic.store.AwsBucket')
    def testTwoUsefulFileInDir(self, mockClass):
        mockClass.return_value.getFileList.return_value = [
            'records RNTIR-00002-RNTIR-01647.js',
            'useless.js',
            'records RNTIR-10002-RNTIR-21647.js'
        ]
        store = Store()
        self.assertEqual(store.getReportFileList(), [
            'records RNTIR-00002-RNTIR-01647.js',
            'records RNTIR-10002-RNTIR-21647.js'
        ])

    @patch('semantic.store.AwsBucket')
    def testgetFilesToProcess(self, mockClass):
        mockClass.return_value.getFileList.return_value = [
            'records RNTIR-00002-RNTIR-01647.js',
            'records RNTIR-00002-RNTIR-01647 processed.js',
            'useless.js',
            'records RNTIR-10002-RNTIR-21647.js'
        ]
        store = Store()
        self.assertEqual(['records RNTIR-10002-RNTIR-21647.js'], store.getFilesToProcess())        



if __name__ == '__main__':
    unittest.main()

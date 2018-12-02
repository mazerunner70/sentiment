import unittest
from unittest.mock import MagicMock, PropertyMock, patch

from loadreviews.csvutils import defineName


class TestCsvUtils(unittest.TestCase):
    def test_name_formatting(self):
        testList = [
            {'key': 'RNTIR-2'},
            {'key': 'RNTIR-1647'},
        ]
        self.assertEqual('records-RNTIR-00002-RNTIR-01647.csv', defineName(testList))
 

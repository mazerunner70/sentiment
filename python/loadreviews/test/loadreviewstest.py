import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from loadreviews.loadreviews import LoadReviews
import sys
print ('124', sys.path)


class TestLoadReviews(unittest.TestCase):
    @patch('loadreviews.loadreviews.AwsBucket')
    def testPrintBucket(self, mockClass):
        instance = mockClass.return_value
        instance.getFileList.return_value = ['elephant']
        print ('098', mockClass)
        LoadReviews().printBucket()

if __name__ == '__main__':
    unittest.main()

import unittest
import json
from unittest.mock import MagicMock, PropertyMock, patch
from os.path import join

from loadreviews.issueiterator import IssueIterator


class TestJiraClient(unittest.TestCase):
    def testOneChunk(self):
        with patch('loadreviews.issueiterator.JiraClient') as mock_object:
            mock_object.return_value.getChunk.return_value = {
                'total' : 4,
                'summaries': [
                    ['KEY-001', "2018-11-14T19:36:59.000+0000", 'Summary 1'],
                    ['KEY-002', "2018-11-15T19:36:59.000+0000", 'Summary 2'],
                    ['KEY-003', "2018-11-16T19:36:59.000+0000", 'Summary 3'],
                    ['KEY-004', "2018-11-17T19:36:59.000+0000", 'Summary 4']
                ]  
                }
            issueIterator = IssueIterator(0)
            for issue in issueIterator:
                print (issue)

    def testTwoChunks(self):
        with patch('loadreviews.issueiterator.JiraClient') as mock_object:
            vals = {tuple((0,)): {
                'total' : 6,
                'summaries': [
                    ['KEY-001', "2018-11-14T19:36:59.000+0000", 'Summary 1'],
                    ['KEY-002', "2018-11-15T19:36:59.000+0000", 'Summary 2'],
                    ['KEY-003', "2018-11-16T19:36:59.000+0000", 'Summary 3']
                ]  
                },tuple((3,)): {
                'total' : 6,
                'summaries': [
                    ['KEY-004', "2018-11-17T19:36:59.000+0000", 'Summary 4'],
                    ['KEY-005', "2018-11-18T19:36:59.000+0000", 'Summary 5'],
                    ['KEY-006', "2018-11-19T19:36:59.000+0000", 'Summary 6']
                ]  
                }   
                }  

            def side_effect(*args):
                print ('221', args, type(args), type (tuple((0,))), vals.get(tuple((0,))))
                print ('225', vals[args])
                return vals[args]
            mock_object.return_value.getChunk = MagicMock(side_effect = side_effect)
            issueIterator = IssueIterator(0)
            for issue in issueIterator:
                print (issue)

if __name__ == '__main__':
    print ('Starting')
    unittest.main()
   


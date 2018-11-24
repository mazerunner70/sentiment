import os
import sys
import unittest
import json
from unittest.mock import MagicMock, PropertyMock, patch
from os.path import join
from loadreviews.jiraclient import JiraClient

class TestJiraClient(unittest.TestCase):
    def setUp(self):
        print('121')
        path = join(os.getcwd(), 'test/files/jira-response.json')
        with open(path, 'r') as textfile:
            self.response = textfile.read()



    def mocked_requests_get(self, *args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data
        res = ''
        path = join(os.getcwd(), 'test/files/jira-response.json')
        with open(path, 'r') as textfile:
            res = textfile.read()
        return MockResponse(json.loads(res), 200)

    def testGetChunk(self):
        with patch('loadreviews.jiraclient.requests.get', side_effect = self.mocked_requests_get, response=self.response ) as mock_get:
            jiraclient = JiraClient()
            result = jiraclient.getChunk(0)
            print ('total:', result['total'])

if __name__ == '__main__':
    print ('Starting')
    unittest.main()

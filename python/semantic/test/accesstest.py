import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from access.access import Access

class TestAccess(unittest.TestCase):
    def test_asrange(self):
        access = Access()
        self.assertEqual(range(0,100000), access.asrange('0-'))

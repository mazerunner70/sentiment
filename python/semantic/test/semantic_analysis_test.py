import unittest
import os
import sys
from subprocess import call
from unittest.mock import MagicMock
from unittest.mock import patch
from semantic.semantic_analysis import SemanticAnalysis

class TestReportIterator(unittest.TestCase):
    def testNoFiles(self):
        nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
        print ('Looking for NLTK at', nltk_data_dir)
        if (not os.path.isdir(nltk_data_dir)):
            print ('Error! cannot find the nltk_data dir at', nltk_data_dir)
            sys.exit(3)
        else:
            print ('If the app complains of not finding corpora, run scripts/load_corpora.bash')
#        call(['printenv'])
        semantic_analysis = SemanticAnalysis()
        print (semantic_analysis.processLine(['','','hello']))
from semantic.store import Store
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
import sys

class SemanticAnalysis:
    def __init__(self, ):
        self.store = Store()
        self.naive_Bayes_analyser = Blobber(analyzer=NaiveBayesAnalyzer())
#        self.naive_Bayes_analyser('def').sentiment
        self.pattern_analyser = Blobber()

    def processFile(self, filename):
        local_input_filename = self.store.filenameAsLocal(filename)
        csv_list = self.store.read_local_csv(local_input_filename)
        local_output_filename = self.store.filenameAsProcessed(local_input_filename)
        output_csv = []
        for line in csv_list:
            pass
            output_csv.append(self.processLine(line))
        self.store.write_local_csv(local_output_filename, output_csv)

    def processLine(self, line):
#        print (self.pattern_analyser('sdfg'))
        print ('12')
        sys.stdout.flush()
#        nb_assessed = self.naive_Bayes_analyser(line[2]).sentiment
        print ('13')
        ptn_assessed = self.pattern_analyser(line[2]).sentiment
        print ('14')
        return [line[0], line[1], '', ptn_assessed.polarity]
#        return [line[0], line[1], nb_assessed.p_pos, ptn_assessed.polarity]
        


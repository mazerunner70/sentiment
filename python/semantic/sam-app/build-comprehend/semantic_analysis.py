from semantic.store import Store
import sys
import boto3

class SemanticAnalysis:
    def __init__(self ):
        self.store = Store()
        self.comprehend_client = boto3.client('comprehend')
        self.batch = []

    def processFile(self, filename):
        local_input_filename = self.store.filenameAsLocal(filename)
        csv_list = self.store.read_local_csv(local_input_filename)
        local_output_filename = self.store.filenameAsProcessed(local_input_filename)
        output_csv = []
        for line in csv_list:
            output_csv.append(self.processLine(line))
        self.store.write_local_csv(local_output_filename, output_csv)

    def processLine(self, line):
        self.batch.append( line.replace('\n',''))
        if len(self.batch) == 25:
            response = self.comprehend_client.batch_detect_sentiment(
                TextList=self.batch,
                LanguageCode='en'
            )
            print( response)
            sys.exit(1)


if __name__ == '__main__':
    pass
        


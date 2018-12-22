from comprehend.store import Store
import sys
import boto3

class SemanticAnalysis:
    def __init__(self ):
        self.store = Store()
        self.comprehend_client = boto3.client('comprehend')

    def processFile(self, filename):
        local_input_filename = self.store.filenameAsLocal(filename)
        csv_list = self.store.read_local_csv(local_input_filename)
        local_output_filename = self.store.filenameAsProcessed(local_input_filename)
        output_csv = []
        for index in range(0, len(csv_list), 25):
            self.processLineBatch(csv_list, index, output_csv)
        self.store.write_local_csv(local_output_filename, output_csv)

    def processLineBatch(self, csv_list, index, output_csv):
        batch = list(map(
            lambda line: line[2].replace('\n',''), 
            csv_list[index, min(index+25, len(csv_list))]
        ))
        response = self.comprehend_client.batch_detect_sentiment(
            TextList=batch,
            LanguageCode='en'
        )
        for i in range(len(batch)):
            csvrow = csv_list[index+i]
            output_csv.append(csvrow[0], csvrow[1], response[i])
        print( index )


if __name__ == '__main__':
    pass
        


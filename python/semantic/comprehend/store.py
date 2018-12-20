from comprehend.awsbucket import AwsBucket
import collections
import re
import os
import csv

class Store:
    def __init__(self):
        self.awsbucket = AwsBucket()
        self.s3_files = self.awsbucket.getFileList()


    def getReportFileList(self):
        pattern = re.compile(r"records-RNTIR-(\d*)-RNTIR-(\d*)\.")
        return list(filter(lambda file: pattern.match(file), self.s3_files))

    def getProcessedFileList(self):
        pattern = re.compile(r"records-RNTIR-(\d*)-RNTIR-(\d*)-comprehend")
        return list(filter(lambda file: pattern.match(file), self.s3_files))

    def getFilesToProcess(self):
        processed = list(map(lambda x: x[0:31], self.getProcessedFileList()))
        print('Processed file stubs ', processed)
        files_to_process = list(filter(lambda x: x[0:31] not in processed, self.getReportFileList()))
        print('Found files to process: ', files_to_process)
        return files_to_process


    def moveFileToLocal(self, filename):
        local_filename = '/tmp/{}'.format(os.path.basename(filename))
        self.awsbucket.download(filename, local_filename)
        return local_filename

    def read_local_csv(self, filename):
        csv_list = []
        with open(self.filenameAsLocal(filename), "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                csv_list.append(row)
        return csv_list

    def write_local_csv(self, filename, csv_list):
        with open(self.filenameAsLocal(filename), "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in csv_list:
                csv_writer.writerow(row)

    def moveFileToS3(self, filename):
        local_filename = self.filenameAsLocal(filename)
        self.awsbucket.upload(local_filename, filename)

    def filenameAsLocal(self,filename):
        return '/tmp/{}'.format(os.path.basename(filename))

    def filenameAsProcessed(self,filename):
        return  filename[:-4]+'-comprehend'+filename[-4:]

if __name__ == '__main__':
    print ('Starting')
    store = Store()
    print(store.s3_files)
    range = store.getReportFileList()
    print (range)
    
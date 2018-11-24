from semantic.store import Store
from semantic.semantic_analysis import SemanticAnalysis

class Semantic:
    def __init__(self):
        self.store = Store()
        self.semantic_analysis = SemanticAnalysis()

    def execute(self):
        files_to_process = self.getFilesToProcess()
        print(f'Found {len(files_to_process)} files to process')
        self.analyseReports(files_to_process)

    def getFilesToProcess(self):
        return self.store.getFilesToProcess()

    def analyseReports(self, files_to_process):
        for filename in files_to_process:
            print(f'Processing "{filename}"')
            self.store.moveFileToLocal(filename)
            self.semantic_analysis.processFile(filename)
#            self.store.moveFileToS3(self.store.filenameAsProcessed(filename))
        
    def processLine(self, line):
        print (line)
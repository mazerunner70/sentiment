from loadreviews.jiraclient import JiraClient

class IssueIterator:
    def __init__(self, startAt):
        self.counter = startAt
        self.total = startAt+1
        self.batch_ctr = 0
        self.batch = []
        self.jiraClient = JiraClient()

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.total:
            if self.batch_ctr == len(self.batch):
                self.nextChunk()
            self.counter += 1
            return self.nextEntry()
        else:
            raise StopIteration()

    def nextChunk(self):
        response = self.jiraClient.getChunk(self.counter)
        self.total = response['total']
        self.batch = response['summaries']
        self.batch_ctr = 0
        if len(self.batch) == 0:
            raise StopIteration()

    def nextEntry(self):
        result = self.batch[self.batch_ctr]
        self.batch_ctr += 1
        return result

            
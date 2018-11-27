import csv
import re


def saveList(list_to_save):
    filename = defineName(list_to_save)
    with open('/tmp/'+filename, 'w') as csv_file:
        line_writer = csv.writer(csv_file)
        for row in list_to_save:
            line_writer.writerow([row['key'], row['created'], row['summary']])
    return filename

def defineName(list_to_save):
    first = int(list_to_save[0]['key'][6:])
    last = int(list_to_save[-1]['key'][6:])
    filename = "records-RNTIR-{lower:05d}-RNTIR-{upper:05d}.csv".format(lower=min(first, last), upper=max(first, last))
    return filename

pattern = re.compile('RNTIR-(\\d*)')
def formatJiraId(self, id):
    matches = pattern.match(id)
    if (matches):
        return 'RNTIR-{05:d}', matches.group(1)


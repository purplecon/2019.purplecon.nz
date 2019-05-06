
import csv
import string

def make_id(title):
    title = title.lower()
    translator = str.maketrans('', '', string.punctuation)
    title = title.translate(translator)
    words = title.split()
    return "-".join(words)


rows = []
with open('schedule.csv', newline='') as csvfile:
     reader = csv.reader(csvfile)
     for row in reader:
         speaker= row[1]
         talkid = make_id(speaker)
         print(talkid)
         row.append(talkid)
         rows.append(row)

with open('schedule-clean.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
        writer.writerow(row)


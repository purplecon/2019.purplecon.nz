import csv
import sys
import string

def make_id(title):
    title = title.lower()
    translator = str.maketrans('', '', string.punctuation)
    title = title.translate(translator)
    words = title.split()
    if "purplecon" in title or "you" in title:
        return ""

    return "-".join(words)


rows = []
with open(sys.argv[1], newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter=",")
     for row in reader:
         speaker= row[1]
         talkid = make_id(speaker)
         time = row[0]
         if not time:
             continue
         print(talkid)
         row.append(talkid)
         rows.append(row)

with open('schedule.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
        writer.writerow(row)


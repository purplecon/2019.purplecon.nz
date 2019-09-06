import csv
import string
import sys

def make_id(title):
    title = title.lower()
    translator = str.maketrans('', '', string.punctuation)
    title = title.translate(translator)
    words = title.split()
    return "-".join(words)

clean_rows = []
with open(sys.argv[1], newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter="\t")
     for row in reader:
         is_accepted = "yes" in row[7].lower()
         title = row[9].strip()
         abstract = row[10].strip()
         speaker = row[11].strip()
         bio = row[12].strip()
         speaker_social = row[13].strip()

         talkid = make_id(speaker)
         clean_row = [talkid,title,abstract,speaker,speaker_social,bio]
         if is_accepted:
             print(talkid, speaker)
             clean_rows.append(clean_row)

with open('talks-clean.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    header = ["talkid","title","abstract","speaker","speaker_social","bio"]
    writer.writerow(header)
    for row in clean_rows:
        writer.writerow(row)


# you have to add the 'id' column and do dos2unix after this lmao yikes

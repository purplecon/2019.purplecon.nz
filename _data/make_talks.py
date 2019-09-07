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
     reader = csv.reader(csvfile, delimiter=",")
     for row in reader:
         is_accepted = "yes" in row[7].lower()
         title = row[9].strip()
         abstract = row[10].strip()
         speaker = row[11].strip()
         bio = row[12].strip()
         speaker_social = row[13].strip()
         is_confirmed = "y" in row[-3].strip().lower()

         talkid = make_id(speaker)
         clean_row = [talkid,title,abstract,speaker,bio]
         if is_accepted and is_confirmed:
             print(talkid, speaker)
             clean_rows.append(clean_row)

with open('talks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    header = ["id","title","description","speaker","bio"]
    writer.writerow(header)
    for row in clean_rows:
        writer.writerow(row)


# you have to add the 'id' column and do dos2unix after this lmao yikes

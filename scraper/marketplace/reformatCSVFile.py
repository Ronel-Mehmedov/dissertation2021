import csv
import requests

f=open("/home/x/dissertation/scraper/marketplace/listToCrawl",'a')


with open('backup.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for entry in row:
            try:
                r = requests.head(entry, timeout=5)
                st1 = entry + "\n"
                f.write(st1)
                print("website {} worked successfully".format(entry))
            except Exception as e:
                print("failed to connect to {}".format(entry))


f.close()


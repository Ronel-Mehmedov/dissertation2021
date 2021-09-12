import csv
import requests

f=open("/home/x/dissertation/data/reformatedCsv",'w')





with open('deliverers.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[1] != "":
            try:
                req = requests.get(row[1])
                r = requests.head(req.url)
                st1 = req.url + "\n"
                f.write(st1)
                print("website {} worked successfully".format(row[1]))
            except requests.ConnectionError:
                print("failed to connect to {}".format(row[1]))


f.close()


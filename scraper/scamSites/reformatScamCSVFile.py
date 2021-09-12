import csv
import requests

f=open("/home/x/dissertation/scraper/scamSites/scamWebsitesToCrawl",'a')


with open('/home/x/dissertation/scraper/scamSites/petscamWebsites.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for entry in row:
            try:
                r = requests.head(entry, timeout=3)
                if r.status_code == 200:
                    st1 = entry + "\n"
                    f.write(st1)
                    print("website {} worked successfully".format(entry))
            except Exception as e:
                print("failed to connect to {}".format(entry))


f.close()


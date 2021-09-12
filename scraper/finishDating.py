import os
import csv
import requests_html
from bs4 import BeautifulSoup

session = requests_html.HTMLSession()

with open('/home/x/dissertation/scraper/nonDatedScamSites.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for entry in row:
            url = entry.replace(".", "-")
            url  = "https://petscams.com/puppy-scammer-list/" + entry
            res = session.get(url)
            soup = BeautifulSoup(res.html.html, "html.parser")
            links = soup.find("small", class_="color-silver-light")
            print("{} : {}".format(entry, links.text))
            dateFile = os.path.join('/home/x/allDataBackup/scamDeliverers', entry)
            if os.path.exists(dateFile):
                dateFileFinal = os.path.join(dateFile, "date")
                with open(dateFileFinal, 'w') as outfile:
                    outfile.write(links.text)
            else:
                print("could not find {}".format(dateFile))
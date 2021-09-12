import os
import csv
from urllib.parse import urlparse

rootDir = "../scamDeliverers/"

def fixName(folderName):
    if "10532" in folderName:
        website = folderName.split("10532")[0]
        return website
    return folderName

dirsList = []
websites = []

for folder in os.scandir(rootDir):
    path = os.path.join(rootDir, folder.name)
    website = fixName(path)
    dirsList.append(fixName(folder.name))

print(dirsList)
print("websites:")


with open('./scamSites/deliverersBatch.csv') as csv_file:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for entry in row:
            websites.append(entry)

print(websites)
for entry in websites:
    flag = False
    for folder in dirsList:
        if folder in entry:
            flag = True
    if flag == False:
        print(entry)
        break

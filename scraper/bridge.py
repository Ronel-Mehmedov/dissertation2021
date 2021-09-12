import os
import csv
from urllib.parse import urlparse



def fixName(folderName):
    if "10532" in folderName:
        website = folderName.split("10532")[0]
        return website
    return folderName

dirsList = []
websites = []


with open('/home/x/histos/zero.csv') as csv_file:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for entry in row:
            dirsList.append(entry)


print(dirsList)
print("websites:")


with open('./scamSites/finalScamDeliverersToCrawl.csv') as csv_file1:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        for entry in row:
            websites.append(entry)

print(websites)

bridgedList = []

for folder in dirsList:
    for entry in websites:
        if folder in entry:
            bridgedList.append(entry)


with open("/home/x/bridgedCSV.csv", 'w') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(bridgedList)

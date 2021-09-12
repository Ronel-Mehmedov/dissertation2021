import os
import csv
import shutil


# rootDir = "../data/"

empty = 0
notEmpty = 0
singleEntry = 0

emptyFoldersList = []
singleFileFolders = []

def fixName(folderName):
    if "10532" in folderName:
        website = folderName.split("10532")[0]
        return website
    return folderName

websites = []
foldersList = []

with open('./marketplace/finalListToCrawl.csv') as csv_file:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for entry in row:
            websites.append(entry)

counter = 0
with open('./emptyFolders.csv') as folders:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(folders, delimiter=',')
    for row in csv_reader:
        for entry in row:
            foldersList.append(entry)
            counter += 1

print(websites)

print(foldersList)
sorted(foldersList)
print(counter)


emptyWebsites = []
for entry in foldersList:
    for website in websites:
        if entry in website:
            emptyWebsites.append(website)



sortedWebsites = sorted(emptyWebsites)


length = 1
previous = sortedWebsites[0]
index = 1
for i in range(1,len(sortedWebsites)):
    if sortedWebsites[i] != previous:
        length += 1
        previous = sortedWebsites[i]
        sortedWebsites[index] = sortedWebsites[i]
        index+=1

print(sortedWebsites)


# for subdir, dirs, files in os.walk(rootDir):

with open('emptyWebsites3.csv', 'w') as empties:
    writer = csv.writer(empties, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(sortedWebsites)

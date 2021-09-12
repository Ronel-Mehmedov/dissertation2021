import os
import csv


rootPath = "/home/x/specialty/scamSites"
# for folder in os.scandir(rootPath):
#     folderPath = os.path.join(rootPath, folder.name)
#     htmlPath = os.path.join(folderPath, "HTML")
#     imagesPath = os.path.join(folderPath, "Images")
#     countPages = 0
#     countImages = 0
#     for file in os.scandir(htmlPath):
#         countPages += 1
#     for img in os.scandir(imagesPath):
#         countImages += 1
#     histo[folder.name] = float(countImages) / float(countPages)
#
#
# rootPath = "/home/x/specialty/scamSites"
# def checkRatio(HTMLPath, imagesPath):

def checkRatio(HTMLPath, imagesPath):
    countPages = 0
    countImages = 0
    for file in os.scandir(HTMLPath):
        countPages += 1
    for img in os.scandir(imagesPath):
        countImages += 1
    return round(float(countImages) / float(countPages), 6)

def getPath(name, scamBin, deliverBin):
    if scamBin == "0" and deliverBin == "0":
        p = os.path.join("/home/x/specialty/marketplace", name)
        return (p + '/HTML', p + '/Images')
    elif scamBin == "1" and deliverBin == "0":
        p = os.path.join("/home/x/specialty/scamSites", name)
        return (p + '/HTML', p + '/Images')
    elif scamBin == "0" and deliverBin == "1":
        p = os.path.join("/home/x/specialty/legitDeliverers", name)
        return (p + '/HTML', p + '/Images')
    elif scamBin == "1" and deliverBin == "1":
        p = os.path.join("/home/x/specialty/scamDeliverers", name)
        return (p + '/HTML', p + '/Images')

map = {}


with open("/home/x/pool/addressAdded2.csv") as csv_file6:
    csv_reader = csv.reader(csv_file6, delimiter=',')
    for row in csv_reader:
        name = row.pop(0)
        map[name] = row

caught = []
count1 = 0

newTable = []
for name, columns in map.items():
    newLine = []
    count1 += 1
    print(count1)
    paths = getPath(name, columns[0], columns[1])
    columns.append(checkRatio(paths[0], paths[1]))
    newLine.append(name)
    for element in columns:
        newLine.append(element)
    newTable.append(newLine)

with open("/home/x/pool/ratiosAdded.csv", 'w') as bs:
    writer = csv.writer(bs, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in newTable:
        writer.writerow(row)

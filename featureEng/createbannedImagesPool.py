import csv
import os
from PIL import Image
import imagehash

pool = []
rootfolder = '/home/x/specialty/scamSites'

with open('/home/x/pool/referenceScamSites.csv') as csv_file1:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        for element in row:
            pool.append(element)

print(pool)

lines = []
for website in pool:
    websitePath = os.path.join(rootfolder, website)
    imagesFolderPath = os.path.join(websitePath, "Images")
    if os.path.exists(imagesFolderPath):
        for item in os.scandir(imagesFolderPath):
            imgPath = os.path.join(imagesFolderPath, item.name)
            try:
                hashCode = imagehash.phash(Image.open(imgPath))
                if hashCode not in lines:
                    lines.append(hashCode)
            except:
                print("error with {}".format(imgPath))
                pass

with open("/home/x/pool/bannedCodes.csv", 'a') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(lines)

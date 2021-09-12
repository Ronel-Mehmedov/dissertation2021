import os
import csv

from PIL import Image

import imagehash

allRows = []
count = 0
rootfolder = '/home/x/specialty/legitDeliverers'
for folder in os.scandir(rootfolder):
    count += 1
    print(count)
    row = [folder.name]
    websitePath = os.path.join(rootfolder, folder.name)
    imagesFolderPath = os.path.join(websitePath, "Images")
    if os.path.exists(imagesFolderPath):
        for item in os.scandir(imagesFolderPath):
            # filename = os.path.join(imagesFolderPath, item.name)
            # try:
            #     im=Image.open(filename)
            # except IOError:
            #     os.remove(filename)
            imgPath = os.path.join(imagesFolderPath, item.name)
            try:
                hashCode = imagehash.phash(Image.open(imgPath))
                row.append(hashCode)
            except:
                print("error with {}".format(imgPath))
                pass
        allRows.append(row)





with open("/home/x/codesForLegitDeliveryIMGS.csv", 'a') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in allRows:
        writer.writerow(i)

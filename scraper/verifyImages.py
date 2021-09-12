import os

from PIL import Image

count = 0

rootfolder = '/home/x/specialty/legitDeliverers'
for folder in os.scandir(rootfolder):
    count += 1
    print(count)
    websitePath = os.path.join(rootfolder, folder.name)
    imagesFolderPath = os.path.join(websitePath, "Images")
    if os.path.exists(imagesFolderPath):
        for item in os.scandir(imagesFolderPath):
            filename = os.path.join(imagesFolderPath, item.name)
            try:
                im=Image.open(filename)
            except IOError:
                os.remove(filename)

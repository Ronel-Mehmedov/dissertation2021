import os

rootfolder = '/home/x/specialty/scamSites'

zero = 0
count = 0

for folder in os.scandir(rootfolder):
    websitePath = os.path.join(rootfolder, folder.name)
    imagesFolderPath = os.path.join(websitePath, "Images")
    if os.path.exists(imagesFolderPath):
        if not os.listdir(imagesFolderPath):
            zero += 1
        for item in os.scandir(imagesFolderPath):
            count += 1
print(zero)
print(count)
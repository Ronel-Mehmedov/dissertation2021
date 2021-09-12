import os

rootPath = "/home/x/specialty/scamSites"
for folder in os.scandir(rootPath):
    folderPath = os.path.join(rootPath, folder.name)
    htmlPath = os.path.join(folderPath, "HTML")
    imagesPath = os.path.join(folderPath, "Images")
    countPages = 0
    countImages = 0
    for file in os.scandir(htmlPath):
        countPages += 1
    for img in os.scandir(imagesPath):
        countImages += 1
    histo[folder.name] = float(countImages) / float(countPages)

for key in histo.keys():
    print("{} : {}".format(key, histo[key])
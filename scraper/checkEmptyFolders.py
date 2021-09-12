import os
import csv
import shutil


rootDir = "../data/"

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


for folder in os.scandir(rootDir):
    path = os.path.join(rootDir, folder.name)
    print(path)
    path = os.path.join(path, "HTML")
    size = os. listdir(path)
    length = len(size)
    print("{} contains {} files".format(folder.name, length))
    if length == 0:
        emptyFoldersList.append(fixName(folder.name))
        print("folder is empty")
        empty += 1
    elif length == 1:
        singleFileFolders.append(fixName(folder.name))
        print("folder has a single entry")
        singleEntry += 1
    else:
        notEmpty += 1
    print("============================")


print("{} empty files".format(empty))

print("{} files are not empty".format(notEmpty))

print("{} files have a single entry".format(singleEntry))

# for subdir, dirs, files in os.walk(rootDir):

with open('emptyFolders.csv', 'w') as empties:
    writer = csv.writer(empties, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(emptyFoldersList)

with open('singleFileFolders.csv', 'w') as singles:
    writer = csv.writer(singles, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(singleFileFolders)



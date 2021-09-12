import os

rootDir = "/home/x/allDataBackup/marketplace"
count = 0
for folder in os.scandir(rootDir):
    folderPath = os.path.join(rootDir, folder.name)
    imagePath = os.path.join(folderPath, "Images")
    if (os.path.exists(imagePath)):
        count += 1

print(count)
import os
from bs4 import BeautifulSoup
import sys
import shutil



rootDir = "/home/x/sss/www.amwat.com.mx"
mode = 0o755

fileStructure = []

for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        pathOfFile = os.path.join(rootDir, subdir)
        pathOfFile = os.path.join(pathOfFile, file)
        if not os.path.exists(pathOfFile):
            print("ERROR - {}".format(pathOfFile))
        else:
            fileTuple = (file, pathOfFile)
            fileStructure.append(fileTuple)

print(fileStructure)

# print(subdir)
# print(dirs)
# print(files)

def checkHTML(pathway):
    if os.path.exists(pathway):
        try:
            checkfile=open(pathway, mode="r", encoding="utf-8")
            ishtml = False
            for line in checkfile:
                line=line.strip()
                if "</html>" in line:
                    ishtml = True
            if ishtml:
                return True
            else:
                return False
        except:
            return False


pathHTML = os.path.join(rootDir, "HTMLFiles")
os.mkdir(pathHTML, mode)
pathImages = os.path.join(rootDir, "ImageFiles")
os.mkdir(pathImages, mode)
pathAllElse = os.path.join(rootDir, "AllElse")
os.mkdir(pathAllElse, mode)

for entry in fileStructure:
    if checkHTML(entry[1]):
        shutil.move(entry[1], os.path.join(pathHTML, entry[0]))



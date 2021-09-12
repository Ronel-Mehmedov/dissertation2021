import os
from html_similarity import style_similarity, structural_similarity, similarity
import csv
from bs4 import BeautifulSoup as bs

def jaccard(first, second):
    min1 = []
    max1 = []
    inter = set(first).intersection(second)
    for s in inter:
        max1.append(max(first[s], second[s]))
        min1.append(min(first[s], second[s]))
    if sum(max1)== 0:
        return 0.0
    return sum(min1) / sum(max1)


def getFreq(path):
    try:
        soup = bs(open(path), "html.parser")
        refDict = {}
        # print(set(tag.name for tag in soup.find_all()))
        for tag in set(tag.name for tag in soup.find_all()):
            refDict[tag] = len(soup.find_all(tag))
        # print(refDict)
        return refDict
    except Exception as E:
        # print(E)
        return {}

referencePaths = []

with open('/home/x/pool/referenceDeliverScamSites.csv') as csv_file1:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        for element in row:
            referencePaths.append(element)

# original = getFreq("/home/x/allDataBackup/scamDeliverers/swiftlinelogistic.com/HTML/!")

maxPeak = 0


docs = []
for element in referencePaths:
    foldPath = "/home/x/specialty/scamDeliverers/{}/HTML".format(element)
    landingPath = foldPath + "/main"
    if os.path.isfile(landingPath):
        landingPage = landingPath
    else:
        landingPage = os.path.join(foldPath, min(os.listdir(foldPath), key=len))
    docs.append(open(landingPage).read())


number = 0
maxVals = {}
for folder in os.scandir("/home/x/test22"):
    print(folder.name)
    htmlPath = os.path.join("/home/x/test22", folder.name + "/HTML")
    mainPathName = os.path.join(htmlPath, "main")
    if os.path.isfile(mainPathName):
        mPage = mainPathName
    else:
        if (len(os.listdir(htmlPath)) == 0):
            continue
        mPage = os.path.join(htmlPath, min(os.listdir(htmlPath), key=len))
    indices = []
    for benchHTML in docs:
        try:
            mainPage = open(mPage).read()
            j = style_similarity(benchHTML, mainPage)
            indices.append(j)
        except Exception as E:
            print(E)
            pass
    maxVals[folder.name] = max(indices, default=0.0)
# if j > 0.8:
#     print("index with {} is : {}".format(filePath, j))

count = 0
for key in maxVals:
    print("{} : {}".format(key, maxVals[key]))
    if (maxVals[key] > 0.8):
        count += 1

print(count)

print(sum(maxVals.values()) / len((maxVals.keys())))


# for key in indexVals.keys():
#     print("{} : {}".format(key, indexVals[key]))





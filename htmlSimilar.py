import os
from html_similarity import style_similarity, structural_similarity, similarity

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


# original = getFreq("/home/x/allDataBackup/scamDeliverers/swiftlinelogistic.com/HTML/!")

maxPeak = 0


docs = []
for doc in os.scandir("/home/x/allDataBackup/scamDeliverers/swiftlinelogistic.com/HTML/"):
    htmlPath = os.path.join("/home/x/allDataBackup/scamDeliverers/swiftlinelogistic.com/HTML/", doc.name)
    docs.append(htmlPath)



maxVals = {}
for folder in os.scandir("/home/x/allDataBackup/legitDeliverers"):
    folderWideIndices = []
    htmlPath = os.path.join("/home/x/allDataBackup/legitDeliverers", folder.name + "/HTML")
    for file in os.scandir(htmlPath):
        indices = []
        filePath = os.path.join(htmlPath, file.name)
        for htmlFile in docs:
            try:
                first = open(htmlFile).read()
                second = open(filePath).read()
                j = similarity(first, second)
                indices.append(j)
            except:
                print("caught error")
        folderWideIndices.append(max(indices, default=0.0))
        # if j > 0.8:
        #     print("index with {} is : {}".format(filePath, j))

    maxVals[folder.name] = max(folderWideIndices, default=0.0)

count = 0
for key in maxVals:
    print("{} : {}".format(key, maxVals[key]))
    if (maxVals[key] > 0.8):
        count += 1

print(count)

print(sum(maxVals.values()) / len((maxVals.keys())))


# for key in indexVals.keys():
#     print("{} : {}".format(key, indexVals[key]))





import os
import csv
from html_similarity import style_similarity, structural_similarity, similarity
import operator

root = "/home/x/specialty/scamDeliverers"

def getMax(dictZ):
    peaks = {}
    for el in dictZ.keys():
        count = 0
        for subElement in dictZ[el].keys():
            if dictZ[el][subElement] > 0.8:
                count += 1
        peaks[el] = count
    print(max(peaks.items(), key=operator.itemgetter(1))[0], count)
    return max(peaks.items(), key=operator.itemgetter(1))[0], count




def getDeleteList(highestDict):
    deleteList = []
    for key in frequencies[highestDict]:
        if frequencies[highestDict][key] > 0.8:
            deleteList.append(key)
    for key in deleteList:
        del frequencies[key]




def getFreq(websiteNamePath):
    auxFreq = {}
    testPage = getMainPage(websiteNamePath)
    # for folder in os.listdir(root):
    for folder in referencePool:
        folderPath = os.path.join(root, folder)
        try:
            compPage = getMainPage(folderPath)
            index = style_similarity(testPage, compPage)
        except:
            index = None
        if index is not None:
            auxFreq[folder] = index
    return auxFreq



def getMainPage(websiteNamePath):
    foldPath = os.path.join(websiteNamePath, "HTML")
    landingPath = foldPath + "/main"

    if os.path.isfile(landingPath):
        landingPage = landingPath
    else:
        landingPage = os.path.join(foldPath, min(os.listdir(foldPath), key=len))

    return open(landingPage, 'r').read()

frequencies = {}

firsthalf = []
with open('/home/x/firstHalf.csv') as csv_file1:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        for element in row:
            firsthalf.append(element)



referencePool = []
with open('/home/x/pool/addHTML/referenceDeliveryHTML.csv') as csv_file2:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file2, delimiter=',')
    for row in csv_reader:
        for element in row:
            referencePool.append(element)


# dictZ = {'a': {'a': 0.1, 'b': 0.2}, 'b': {'a': 0.3, 'b': 0.9, 'c': 0.9}, 'c': {'3': 0.3, '4': 0.9}, 'd': {'3': 0.3, '4': 0.9}}


count = 0
for folder in os.listdir("/home/x/specialty/scamDeliverers"):
    print(folder)
    count += 1
    print(count)
    folderPath = os.path.join('/home/x/specialty/scamDeliverers', folder)
    try:
        frequencies[folder] = getFreq(folderPath)
    except:
        pass
table = []
for website in frequencies.keys():
    line = []
    line.append(website)
    for connection in frequencies[website].keys():
        line.append(connection)
        line.append(frequencies[website][connection])
    table.append(line)



# with open("/home/x/pool/addHTML/legitDeliveryHTMLs.csv", 'w') as b:
#     writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row in table:
#         writer.writerow(row)




countMax = 100
mapping = []
while(countMax > 2):
    highestKey, countMax = getMax(frequencies)
    print("{} : {}".format(highestKey, countMax))
    mapping.append((highestKey, countMax))
    getDeleteList(highestKey)

print("printing mapping")


#




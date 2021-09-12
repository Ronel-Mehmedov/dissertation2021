import csv
import os
import operator


def getMax(dictZ):
    peaks = {}

    for el in dictZ.keys():
        count = 0

        for subElement in dictZ[el].keys():
            if dictZ[el][subElement] > 0.80:
                count += 1
        peaks[el] = count
        answer = sorted(peaks.items(), key=lambda item: item[1], reverse=True)[0]
    return answer[0], answer[1]

def getminiMax(dictZ):
    return max(dictZ.values())

def getHTMLTable(path):
    blankDict = {}
    with open(path) as csv_file1:
        csv_reader = csv.reader(csv_file1, delimiter=',')
        for row in csv_reader:
            name = row.pop(0)
            subFreq = {}
            while(len(row) > 0):
                key = row.pop(0)
                value = float(row.pop(0))
                subFreq[key] = value
            blankDict[name] = subFreq

    HTMLdict = {}
    for key in blankDict.keys():
        HTMLdict[key] = round(getminiMax(blankDict[key]), 5)
    return HTMLdict

def getValToInsert(name, scamBin, deliverBin):
    if scamBin == "0" and deliverBin == "0":
        try:
            return marketplaceDict[name]
        except:
            return []
    elif scamBin == "1" and deliverBin == "0":
        try:
            return scamSitesDict[name]
        except:
            return []
    elif scamBin == "0" and deliverBin == "1":
        try:
            return legitDeliverersDict[name]
        except:
            return []
    elif scamBin == "1" and deliverBin == "1":
        try:
            return scamDeliverersDict[name]
        except:
            return []



marketplaceDict = getHTMLTable('/home/x/pool/addHTML/frequenciesForMarketplace23.csv')
scamSitesDict = getHTMLTable('/home/x/pool/addHTML/frequenciesForScams23.csv')
scamDeliverersDict = getHTMLTable('/home/x/pool/addHTML/DeliveryHTMLs.csv')
legitDeliverersDict = getHTMLTable('/home/x/pool/addHTML/legitDeliveryHTMLs.csv')

print(legitDeliverersDict)


currTable = []
with open('/home/x/pool/addHTML/imagesAddedNoOverlap.csv') as csv_file6:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file6, delimiter=',')
    for row in csv_reader:
        currTable.append(row)


# for key, value in HTMLdict.items():
#     print(key, value)
with open("/home/x/pool/HTMLadded.csv", 'w') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in currTable:
        row.append(getValToInsert(row[0], row[1], row[2]))
        writer.writerow(row)


#






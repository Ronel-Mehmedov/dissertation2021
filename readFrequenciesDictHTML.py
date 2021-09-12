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




def getDeleteList(highestDict):
    deleteList = []
    for key in frequenciesDict[highestDict]:
        if frequenciesDict[highestDict][key] > 0.8:
            deleteList.append(key)
    for key in deleteList:
        if key in frequenciesDict.keys():
            del frequenciesDict[key]



frequenciesDict = {}


with open('/home/x/freqForDeliveryHTML.csv') as csv_file1:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        name = row.pop(0)
        subFreq = {}
        while(len(row) > 0):
            key = row.pop(0)
            value = float(row.pop(0))
            subFreq[key] = value
        frequenciesDict[name] = subFreq


countMax = 100
mapping = []
while(countMax > 2):
    highestKey, countMax = getMax(frequenciesDict)
    print("{} - {}".format(highestKey, countMax))
    mapping.append((highestKey, countMax))
    getDeleteList(highestKey)






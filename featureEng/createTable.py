import os
import csv

def getCodes(name, scamBin, deliverBin):
    if scamBin == "0" and deliverBin == "0":
        return marketplaceDict[name]
    elif scamBin == "1" and deliverBin == "0":
        return scamSitesDict[name]
    elif scamBin == "0" and deliverBin == "1":
        try:
            return legitDeliverersDict[name]
        except:
            return []
    elif scamBin == "1" and deliverBin == "1":
        return scamDeliverersDict[name]



def getFeatureVal(row):
    codes = getCodes(row[0], row[1], row[2])
    if len(codes) == 0:
        return "NA"
    flag = False
    for code in codes:
        for banned in bannedCodes:
            if code == banned:
                flag = True
    if flag is True:
        return "1"
    else:
        return "0"


bannedCodes = []

with open('/home/x/pool/bannedCodesNoOverlap.csv') as csv_file6:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file6, delimiter=',')
    for row in csv_reader:
        for entry in row:
            bannedCodes.append(entry)

# rootfolder = "/home/x/specialty/scamDeliverers"
#
#
# with open("/home/x/featuresTable.csv", 'a') as b:
#     writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for folder in os.scandir(rootfolder):
#         line = []
#         line.append(folder.name)
#         line.append("1")
#         line.append("1")
#         writer.writerow(line)
#
# #
marketplaceDict = {}
legitDeliverersDict = {}
scamDeliverersDict = {}
scamSitesDict = {}

with open('/home/x/codesForIMGS.csv') as csv_file1:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        try:
            name = row[0]
            row.pop(0)
            marketplaceDict[name] = row
        except:
            print("{}: line is empty". format(row))

with open('/home/x/codesForScamIMGS.csv') as csv_file2:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file2, delimiter=',')
    for row in csv_reader:
        try:
            name = row[0]
            row.pop(0)
            scamSitesDict[name] = row
        except:
            print("{}: line is empty". format(row))

with open('/home/x/codesForScamDeliveryIMGS.csv') as csv_file3:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file3, delimiter=',')
    for row in csv_reader:
        try:
            name = row[0]
            row.pop(0)
            scamDeliverersDict[name] = row
        except:
            print("{}: line is empty". format(row))

with open('/home/x/codesForLegitDeliveryIMGS.csv') as csv_file4:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file4, delimiter=',')
    for row in csv_reader:
        try:
            name = row[0]
            row.pop(0)
            legitDeliverersDict[name] = row
        except:
            print("{}: line is empty". format(row))



newTable = []

with open('/home/x/pool/filteredTable.csv') as csv_file5:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file5, delimiter=',')
    for row in csv_reader:
        newLine = []
        row.append(getFeatureVal(row))
        newTable.append(row)


with open("/home/x/pool/imagesAddedNoOverlap.csv", 'w') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for entry in newTable:
        writer.writerow(entry)






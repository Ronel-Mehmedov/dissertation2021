import csv
import os

def getValToInsert(scamBin, deliverBin):
    if scamBin == "0" and deliverBin == "0":
        return 0
    elif scamBin == "1" and deliverBin == "0":
        return 1
    elif scamBin == "0" and deliverBin == "1":
        return 0
    elif scamBin == "1" and deliverBin == "1":
        return 1



responseVector = []
newTable = []
with open('/home/x/pool/menu/matrix/menuAdded(delivery).csv') as csv_file6:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file6, delimiter=',')
    for row in csv_reader:
        row.pop(0)
        scamOrNot = row.pop(0)
        row.pop(0)
        responseVector.append(scamOrNot)

        if row[0] == "NA":
            row[0] = '0'
        print(row[0])
        if row[4] == "-1":
            row[4] = 0.0
        row[4] = round(float(row[4]), 6)
        newTable.append(row)


with open("/home/x/pool/menu/matrix/responseVector(delivery).csv", 'w') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in responseVector:
        writer.writerow(row)

with open("/home/x/pool/menu/matrix/featuresMatrix(delivery).csv", 'w') as c:
    writer = csv.writer(c, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in newTable:
        writer.writerow(row)


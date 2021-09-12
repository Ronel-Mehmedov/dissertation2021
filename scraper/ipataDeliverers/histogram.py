import os
import csv

zerosList = []
onesList = []
twosList = []
threesList = []
foursList = []
fiveTenList = []
tensList = []
twentyList = []
thirtyList = []
fourtyList = []
fiftyList = []
sixtyList = []
seventyList = []
hundredList = []




for folder in os.scandir("/home/x/scamSitesFollow"):
    count = 0
    initPath = os.path.join("/home/x/scamSitesFollow", folder.name)
    htmlPath = os.path.join(initPath, "HTML")
    for file in os.scandir(htmlPath):
        count += 1

    if count == 0:
        zerosList.append(folder.name)
    elif count == 1:
        onesList.append(folder.name)
    elif count == 2:
        twosList.append(folder.name)
    elif count == 3:
        threesList.append(folder.name)
    elif count == 4:
        foursList.append(folder.name)
    elif count > 4 and count <= 10:
        fiveTenList.append(folder.name)
    elif count > 10 and count <= 20:
        tensList.append(folder.name)
    elif count > 20 and count <= 30:
        twentyList.append(folder.name)
    elif count > 30 and count <= 40:
        thirtyList.append(folder.name)
    elif count > 40 and count <= 50:
        fourtyList.append(folder.name)
    elif count > 50 and count <= 60:
        fiftyList.append(folder.name)
    elif count > 60 and count <= 70:
        sixtyList.append(folder.name)
    elif count > 70 and count <= 150:
        seventyList.append(folder.name)
    elif count > 150:
        hundredList.append(folder.name)


with open('/home/x/histos/zero.csv', 'w') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(zerosList)

with open('/home/x/histos/one.csv', 'w') as one:
    writer = csv.writer(one, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(onesList)

with open('/home/x/histos/two.csv', 'w') as two:
    writer = csv.writer(two, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(twosList)

with open('/home/x/histos/three.csv', 'w') as three:
    writer = csv.writer(three, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(threesList)

with open('/home/x/histos/four.csv', 'w') as four:
    writer = csv.writer(four, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(foursList)

with open('/home/x/histos/fiveToTen.csv', 'w') as fiveToTen:
    writer = csv.writer(fiveToTen, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(fiveTenList)

with open('/home/x/histos/tens.csv', 'w') as tens:
    writer = csv.writer(tens, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(tensList)

with open('/home/x/histos/twenties.csv', 'w') as twenties:
    writer = csv.writer(twenties, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(twentyList)

with open('/home/x/histos/thirties.csv', 'w') as thirties:
    writer = csv.writer(thirties, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(thirtyList)

with open('/home/x/histos/forties.csv', 'w') as forties:
    writer = csv.writer(forties, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(fourtyList)

with open('/home/x/histos/fiftys.csv', 'w') as fiftys:
    writer = csv.writer(fiftys, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(fiftyList)

with open('/home/x/histos/sixtys.csv', 'w') as sixtys:
    writer = csv.writer(sixtys, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(sixtyList)

with open('/home/x/histos/seventy.csv', 'w') as seventy:
    writer = csv.writer(seventy, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(seventyList)

with open('/home/x/histos/hundred.csv', 'w') as hundred:
    writer = csv.writer(hundred, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(hundredList)

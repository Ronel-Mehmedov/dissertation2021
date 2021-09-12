import csv
bannedCodes = []

legitHashes= []
with open('/home/x/pool/bannedCodes.csv') as csv_file6:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file6, delimiter=',')
    for row in csv_reader:
        for entry in row:
            bannedCodes.append(entry)

marketplaceDict = {}

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


count = 0
overlapped = []
for code in bannedCodes:
    for key in marketplaceDict.keys():
        row  = marketplaceDict[key]
        if code in row:
            count += 1
            print("{} found in {}".format(code, key))
            overlapped.append(code)
            continue

bannedCodesNoOverlap = []

for shared in overlapped:
    for valueList in marketplaceDict.values():
        for entry in valueList:
            if shared == entry:
                if shared not in bannedCodesNoOverlap:
                    bannedCodesNoOverlap.append(shared)
                    continue

finalCodes = []
for banned2 in bannedCodes:
    flag = False
    for bn2 in bannedCodesNoOverlap:
        if banned2 == bn2:
            flag = True
    if flag == False:
        finalCodes.append(banned2)



with open("/home/x/pool/bannedCodesNoOverlap.csv", 'w') as x:
    writer = csv.writer(x, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(finalCodes)


print(len(bannedCodes))
print(count)
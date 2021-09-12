import csv

codes = {}
with open('/home/x/codesForScamIMGS.csv') as csv_file1:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        banList = []
        for i in range(len(row)):
            if i > 0 and row[i] not in banList:
                codes[row[i]] = codes.get(row[i], 0) + 1
                banList.append(row[i])
        banList.clear()

i = 0
targetCodesList = []

for pair in dict(sorted(codes.items(), key=lambda item: item[1])):
    print(pair, codes.get(pair))
    i += 1
    if i > 5620:
        targetCodesList.append(pair)
print(i)

# for pair in dict(sorted(codes.items(), key=lambda item: item[1])):
#     print(pair, codes.get(pair))
#     i += 1
#     if i > 21472:
#         targetCodesList.append(pair)
# #
# with open("/home/x/targetDeliveryHashCodes.csv", 'w') as b:
#     writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(targetCodesList)


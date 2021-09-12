import csv
count = 0

banned = []

with open('/home/x/pool/common.csv') as csv_file1:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        for entry in row:
            banned.append(entry)

filteredTable = []
with open('/home/x/featuresTable.csv') as csv_file2:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file2, delimiter=',')
    for row in csv_reader:
        # if row[0] == ""
        legit = True
        for ban in banned:
            if row[0] == ban:
                legit = False
        if legit == True:
            filteredTable.append(row)

print(len(filteredTable))

with open("/home/x/pool/filteredTable.csv", 'w') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for entry in filteredTable:
        writer.writerow(entry)




import csv

legits = 0
scams = 0

with open('/home/x/pool/imagesAddedNoOverlap.csv') as csv_file6:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file6, delimiter=',')
    for row in csv_reader:
        if row[3] == "1" and row[1] == "0" and row [2] == "0":
            legits += 1
        if row[3] == "1" and row[1] == "1" and row [2] == "0":
            scams += 1

print(legits)

print(scams)
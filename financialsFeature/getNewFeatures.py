import csv
import os

map = {}
with open("/home/x/pool/financial/financialData.csv") as csv_file6:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file6, delimiter=',')
    for row in csv_reader:
        name = row.pop(0)
        map[name] = row

miniMatrix = []

for key in map.keys():
    line = []
    if len(map[key]) == 0:
        line.append(0)
        




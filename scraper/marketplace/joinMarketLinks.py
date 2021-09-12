import csv

data = []

with open('legitWebsites.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for site in row:
            data.append(site)

with open('FixedLinks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for site in row:
            data.append(site)


with open('marketplaceLinks.csv', 'a') as brokenLinks:
    writer = csv.writer(brokenLinks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(data)


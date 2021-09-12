import csv

counter = 0

with open('finalMarketLinks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for site in row:
            counter += 1

print(counter)

# prohibited = ["@", "instag", "facebook", "marketplace"]
#
# data = []
# finalVersion = []
#
# def checks(element):
#     for item in prohibited:
#         if item in element.lower():
#             return False
#     return True
#
#
# with open('marketplaceLinks.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for row in csv_reader:
#         for site in row:
#             data.append(site)
#
# duplicateFree = list(set(data))
#
# for entry in duplicateFree:
#     if checks(entry):
#         finalVersion.append(entry)
#
# with open('finalMarketLinks.csv', 'a') as links:
#     writer = csv.writer(links, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(finalVersion)




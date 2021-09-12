import os
import csv

root = "/home/x/specialty/marketplace"
first = []
i = 0
for website in os.listdir(root):
    if i < 2:
        first.append(website)
        i += 1

with open("/home/x/firstHalf.csv", 'w') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(first)


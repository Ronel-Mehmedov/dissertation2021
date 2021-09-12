import os
import csv
import re
from bs4 import BeautifulSoup
from bs4.element import Comment



map2 = {}


sharedImages = []
htmlSimilarity = []
addressFound = []
imagesRatio = []
scamMenu = []
fin = []


with open("/home/x/pool/menu/matrix/addFinancials/featuresMatrixFin(delivery).csv") as csv_file6:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file6, delimiter=',')
    for row in csv_reader:
        sharedImages.append(row.pop(0))
        htmlSimilarity.append(row.pop(0))
        addressFound.append(row.pop(0))
        imagesRatio.append(row.pop(0))
        scamMenu.append(row.pop(0))
        fin1 = []
        fin1.append((row.pop(0)))
        fin1.append((row.pop(0)))
        fin1.append((row.pop(0)))
        fin.append(fin1)

sharedImages.pop(0)
htmlSimilarity.pop(0)
addressFound.pop(0)
imagesRatio.pop(0)
scamMenu.pop(0)

# with open("/home/x/pool/menu/matrix/single/financialFeatures.csv", 'w') as a:
#     writer = csv.writer(a, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row in fin:
#         writer.writerow(row)
#
# with open("/home/x/pool/menu/matrix/single/sharedImages.csv", 'w') as a:
#     writer = csv.writer(a, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row in sharedImages:
#         writer.writerow(row)
#
#
# with open("/home/x/pool/menu/matrix/single/htmlSimilarity.csv", 'w') as b:
#     writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row in htmlSimilarity:
#         writer.writerow([round(float(row), 6)])
#
with open("/home/x/pool/menu/matrix/single/addressFound.csv", 'w') as c:
    writer = csv.writer(c, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in addressFound:
        writer.writerow(row)
#
# with open("/home/x/pool/menu/matrix/single/imagesRatio.csv", 'w') as d:
#     writer = csv.writer(d, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row in imagesRatio:
#         writer.writerow([round(float(row), 6)])
#
# with open("/home/x/pool/menu/matrix/single/scamMenu.csv", 'w') as e:
#     writer = csv.writer(e, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for row in scamMenu:
#         writer.writerow([round(float(row), 6)])
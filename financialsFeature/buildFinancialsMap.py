import os
import csv
import re
from bs4 import BeautifulSoup
from bs4.element import Comment

map = {}

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

def getPath(name, scamBin, deliverBin):
    if scamBin == "0" and deliverBin == "0":
        p = os.path.join("/home/x/specialty/marketplace", name)
        return (p + '/HTML')
    elif scamBin == "1" and deliverBin == "0":
        p = os.path.join("/home/x/specialty/scamSites", name)
        return (p + '/HTML')
    elif scamBin == "0" and deliverBin == "1":
        p = os.path.join("/home/x/specialty/legitDeliverers", name)
        return (p + '/HTML')
    elif scamBin == "1" and deliverBin == "1":
        p = os.path.join("/home/x/specialty/scamDeliverers", name)
        return (p + '/HTML')

map = {}
with open("/home/x/pool/menu/menuAdded.csv") as csv_file6:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file6, delimiter=',')
    for row in csv_reader:
        name = row[0]
        map[name] = row


financialData = []
for folder in map.keys():
    line = []
    print(folder)
    folderWidePrices = []
    folderPath = getPath(folder, map[folder][1], map[folder][2])
    for file in os.listdir(folderPath):
        filePath = os.path.join(folderPath, file)
        try:
            text = open(filePath, 'r').read()
        except UnicodeDecodeError:
            text = ""
        results = re.findall('\d+\.?\d+[$£€¥]|[$£€¥]\d+\.?\d+', text_from_html(text))
        for result in results:
            result.replace(" ", "")
            result.replace(",", ".")
            result = "".join(c for c in result if c not in ['$','£','€','¥'])
            folderWidePrices.append(result)
    line.append(folder)
    for price in folderWidePrices:
        line.append(price)
    financialData.append(line)


# print(count)
#
with open("/home/x/pool/financial/financialData.csv", 'w') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in financialData:
        writer.writerow(row)
import re
import os
import csv
import operator
from bs4 import BeautifulSoup
from bs4.element import Comment

regexList = ['\s[\w\d]*\s\d{5}[-\s]?(?:[0-9]{4})?\s[\w\d]*\s?', '\s[\w\d]*\s\d{5}[-\s]?(?:[0-9]{4})?$']

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
        return os.path.join("/home/x/specialty/marketplace", name) + '/HTML'
    elif scamBin == "1" and deliverBin == "0":
        return os.path.join("/home/x/specialty/scamSites", name) + '/HTML'
    elif scamBin == "0" and deliverBin == "1":
        return os.path.join("/home/x/specialty/legitDeliverers", name) + '/HTML'
    elif scamBin == "1" and deliverBin == "1":
        return os.path.join("/home/x/specialty/scamDeliverers", name) + '/HTML'


def checkRegex(regex, text):
    resultList = re.findall(regex, text)

    for result in resultList:
        if len(result) > 0:
            return True
        else:
            return False


#
# regexList = ['^\d{5}[-\s]?(?:[0-9]{4})?$', '\D\d{5}[-\s]?(?:[0-9]{4})?$', '\D\d{5}[-\s]?(?:[0-9]{4})?\D', '^\d{5}[-\s]?(?:[0-9]{4})?\D', '^[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}$', '\D[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}$', '\D[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}\D', '^[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}\D']

def checkForPostCode(text):
    for regex in regexList:
        if checkRegex(regex, text) == True:
            return True
    return False

# HTMLString = open("/home/x/specialty/scamSites/affordablebengalss.com/HTML/!", 'r').read()



map = {}


with open("/home/x/pool/HTMLadded2.csv") as csv_file6:
    csv_reader = csv.reader(csv_file6, delimiter=',')
    for row in csv_reader:
        name = row.pop(0)
        map[name] = row

caught = []
count1 = 0

newTable = []
for name, columns in map.items():
    newLine = []
    postCodeFound = False
    count1 += 1
    print(count1)
    HTMLPath = getPath(name, columns[0], columns[1])
    # if HTMLPath == "/home/x/specialty/legitDeliverers/huskypupshome.com/HTML":
    #     print("s")
    for file in os.listdir(HTMLPath):
        filePath = os.path.join(HTMLPath, file)
        text = open(filePath, 'rb').read()
        if checkForPostCode(text_from_html(text)) == True:
            postCodeFound = True
            columns.append("1")
            break
    if postCodeFound == False:
        columns.append("0")
    newLine.append(name)
    for element in columns:
        newLine.append(element)
    newTable.append(newLine)

with open("/home/x/pool/addressAdded.csv", 'w') as bs:
    writer = csv.writer(bs, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in newTable:
        writer.writerow(row)


# first = " 12345 "
#
#
# print(re.findall('\s[\w\d]*\s\d{5}[-\s]?(?:[0-9]{4})?\s[\w\d]*\s?', first))
# print(re.findall('\s[\w\d]*\s\d{5}[-\s]?(?:[0-9]{4})?$', first))


# '\D\d{5}[-\s]?(?:[0-9]{4})?$'
# '\D\d{5}[-\s]?(?:[0-9]{4})?\D'
# ^\d{5}[-\s]?(?:[0-9]{4})?\D'


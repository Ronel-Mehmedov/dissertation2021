from extractAllLinks import *
# from seleniumScraper2 import *
import urllib.request
from urllib.request import Request, urlopen
import os
import csv
import traceback


altName = 105323


def get_html(url, page, mainWebsite, htmlPath):
    leafName = url.split(mainWebsite)[-1]
    leafName = leafName.replace("/", "??")
    if leafName == "":
        leafName = "main"
    leafPath = os.path.join(htmlPath, leafName)
    f=open(leafPath,'wb')
    # pagetext=page.read()
    # f.write(pagetext)
    f.write(page)
    f.close()



websites = []

with open('./ipataDeliverers/demo.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for entry in row:
            websites.append(entry)


for website in websites:
    domain_name = urlparse(website).netloc.replace("www.", "")
    print("domain name is {}".format(domain_name))
    parsed_href = urlparse(website)
    print("name of folder is {}".format(parsed_href.netloc))
    folderName = parsed_href.netloc
    parent_dir = "/home/x/dissertation/data"
    mode = 0o755
    path = os.path.join(parent_dir, folderName)
    try:
        os.mkdir(path, mode)
    except:
        newName = parsed_href.netloc + str(altName)
        path = os.path.join(parent_dir, newName)
        os.mkdir(path, mode)
        altName += 1
    htmlPath = os.path.join(path, "HTML")
    os.mkdir(htmlPath, mode)
    try:
        internalLinks, externalLinks, headers = execute(website, domain_name)
    except:
        internal_urls.clear()
        external_urls.clear()
        visited.clear()


    for link in internalLinks:
        try:
            print("link is {}".format(link))
            reqq = Request(link, headers={"User-Agent": "XY"})
            page = urlopen(reqq).read()
            get_html(link, page, website, htmlPath)
        except Exception as e:
            print(e)
            print("website {}  - 404".format(link))

    externalLinksFileName = os.path.join(path, "externalLinks.csv")
    with open(externalLinksFileName, 'a') as b:
        writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(externalLinks)

    headersFile = os.path.join(path, "headers")
    with open(headersFile, 'w') as outfile:
        outfile.write(str(headers))


    internal_urls.clear()
    external_urls.clear()
    visited.clear()


# websitesToCrawl = ["https://www.mysticalpoodles.com/"]
#
# for website in websitesToCrawl:
#     folderName = website.split(".")[1]
#     innerLinks = execute(website)
#     parent_dir = "/home/x/dissertation/data"
#     mode = 0o755
#     path = os.path.join(parent_dir, folderName)
#     os.mkdir(path, mode)
#     for innerLink in innerLinks:
#         leafName = innerLink.split(website)[-1]
#         leafName = leafName.replace("/", "??")
#         if leafName == "":
#             leafName = "main"
#         leafPath = os.path.join(path, leafName)
#         os.mkdir(leafPath, mode)


# folderName = url.split(".")[1]
# baseName = "/home/x/dissertation/data/"
# path = os.path.join(baseName, folderName)


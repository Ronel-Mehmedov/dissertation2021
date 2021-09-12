import os
import csv
import requests_html
from bs4 import BeautifulSoup

session = requests_html.HTMLSession()
homeFolder = "/home/x/allDataBackup/scamDeliverers"
#
# with open('/home/x/dissertation/scraper/scamSites/petscamWebsites.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for row in csv_reader:
#         for entry in row:
#             entry = entry.replace("https://", "")
#             entry = entry.lower()

#
#

websites = []

foldersList = []
foundCount = 0
i = 2

while i <= 94:
    # urlToPass = "https://petscams.com/category/puppy-scammer-list/page/{}/".format(i)
    urlToPass = "https://petscams.com/category/pet-delivery-agency/page/{}/".format(i)
    res = session.get(urlToPass)
    soup = BeautifulSoup(res.html.html, "html.parser")
    links = soup.find_all("div", class_="poster-text")
    for link in links:
        pair = {}

        name = link.find("h4", recursive=True)
        name = name.text.lower()
        date1= link.find("span", recursive=True)
        pair[name] = date1.text
        websites.append(pair)



    #
    # websites1 = driver.find_elements_by_class_name('col-md-6.column-first')
    # websites2 = driver.find_elements_by_class_name('col-md-6.column-second')
    #
    # websites = [websites1, websites2]
    #
    # for website in websites:
    #     for w in website:
    #         s = w.find_element_by_tag_name("h4").text
    #         s = s[0].lower() + s[1:]
    #         # s = link.get_attribute('href')
    #         s = "https://" + s
    #         data.append(s)

    i += 1

# for website in websites:
#     for key in website:
#         print("{} : {}".format(key, website[key]))

for folder in os.scandir(homeFolder):
    for website in websites:
        for key in website:
            if key == folder.name:
                dateFile = os.path.join(homeFolder, folder.name)
                dateFile = os.path.join(dateFile, "date")
                with open(dateFile, 'w') as outfile:
                    outfile.write(website[key])




# count = 0
# for folder in os.scandir(homeFolder):
#     foldersList.append(folder.name)
#     count += 1
#
# myDict = {}
# for f in foldersList:
#     hits = []
#     for website1 in websites:
#         if f == website1:
#             hits.append(website1)
#     myDict[f] = hits
#
# prov = 0
#
# for i in sorted (myDict.keys()) :
#     print("{} : {}".format(i, myDict[i]))
#     if (len(myDict[i]) != 0):
#         prov += 1
#
#
# print(prov)

# finalCount = 0
# for key, values in myDict.items():
#     if (len(values) > 1):
#         print("{} : {}".format(key, values))
#         finalCount += 1
#
#
# for key, values in myDict.items():
#     if (len(values) > 1):
#         print("{} : {}".format(key, values))
#         finalCount += 1
#
# print("++++++++++++++++++++++++++++++++++++++++")
# print("printing empty vals")
# finalCount1 = 0
# for key, values in myDict.items():
#     if (len(values) == 0):
#         print("could not find website for folder {}".format(key))
#         finalCount1 += 1
#
#
#
#
# ones = 0
#
# for key, values in myDict.items():
#     if (len(values) == 1):
#         print("{} : {}".format(key, values))
#         ones += 1
#
# print("{} folders with 0 hits".format(finalCount1))
# print("{} folders with multiple hits".format(finalCount))
# print("{} folders with single hit".format(ones))
# print("total folders - {}".format(count))
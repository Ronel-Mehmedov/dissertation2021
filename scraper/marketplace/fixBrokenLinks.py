import time
import csv
from selenium import webdriver


def correctLink(text):
    stripped = text.split("breeder/", 1)[1]
    breederName = stripped.split("/")[0]
    fullPath = "https://marketplace.akc.org/breeder/" + breederName
    return fullPath




correctLinks = []
noPuppies = []
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#
def getwebsites(row):
    counter = 0
    for site in row:
        if "coming-soon" in site:
            correctedURL = correctLink(site)
            driver.get(correctedURL)
            time.sleep(1)
            try:
                label = driver.find_element_by_class_name("basic-operations")
                links = label.find_elements_by_tag_name("a")
                for link in links:
                    if "http" in link.text and "marketplace" not in link.text:
                        correctLinks.append(link.text)
                        counter += 1
                        print(counter)
                        print(link.text)
            except:
                noPuppies.append(site)


with open('brokenLinks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        getwebsites(row)

with open('FixedLinks.csv', 'a') as legitWebsites:
    writer = csv.writer(legitWebsites, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(correctLinks)

with open('NoPuppies.csv', 'a') as brokenLinks:
    writer = csv.writer(brokenLinks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(noPuppies)


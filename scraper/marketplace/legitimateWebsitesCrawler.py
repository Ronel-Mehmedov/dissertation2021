import time
import csv

from selenium import webdriver


data = []
broken = []
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

def getwebsites(row):
    counter = 0
    for site in row:
        driver.get(site)
        time.sleep(1)
        try:
            label = driver.find_element_by_class_name("basic-operations")
            links = label.find_elements_by_tag_name("a")
            for link in links:
                if "http" in link.text:
                    data.append(link.text)
                    counter += 1
                    print(counter)
                    print(link.text)
        except:
            broken.append(site)

total = 0

with open('linksToLegitWebsites.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for element in row:
            total += 1

print(total)
twentieth = int(total / 20)
print(twentieth)

beginning = 19 * twentieth
end = 20 * twentieth
print(beginning)
print(end)

with open('linksToLegitWebsites.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        getwebsites(row[beginning:])


with open('legitWebsites.csv', 'a') as legitWebsites:
    writer = csv.writer(legitWebsites, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(data)

with open('brokenLinks.csv', 'a') as brokenLinks:
    writer = csv.writer(brokenLinks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(broken)


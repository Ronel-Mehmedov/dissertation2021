import time
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

driver.get("https://www.ipata.org/ipata-pet-ground-transporters")

search = driver.find_element_by_id("search-by-company")


search.send_keys(Keys.RETURN)
time.sleep(5)

data = []

companies = driver.find_elements_by_class_name('active-head')
detailedInfo = driver.find_elements_by_class_name('slide-box')
i = 0

commonParent = driver.find_elements_by_class_name('even.liste')

for a in commonParent:
    company = a.find_element_by_class_name('active-head')
    print(company.find_element_by_class_name('small-5.columns').text)
    compName = company.find_element_by_class_name('small-5.columns').text

    detailedInfo = a.find_element_by_class_name('slide-box')
    rawInfo = detailedInfo.find_element_by_class_name('medium-5.columns')
    links = rawInfo.find_elements_by_tag_name("a")
    website = ''
    for link in links:
        s = link.get_attribute('href')
        if 'http' in s:
            print(s)
            website = s
    result = (compName, website)
    data.append(result)

print(data)

# for company in companies:
#     raw = company.find_element_by_class_name('small-5.columns').text
#     print(raw)
#
# for d in detailedInfo:
#     rawInfo = d.find_element_by_class_name('medium-5.columns')
#     links = rawInfo.find_elements_by_tag_name("a")
#     for link in links:
#         s = link.get_attribute('href')
#         if 'http' in s:
#             print(s)
#
#
with open('deliverers.csv', mode='w') as deliverers:
    writer = csv.writer(deliverers, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for entry in data:
        writer.writerow([entry[0], entry[1]])


with open('deliverers.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(f'\t{row[0]} , {row[1]}')
        line_count += 1

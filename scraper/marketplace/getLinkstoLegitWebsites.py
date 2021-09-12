import time
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

data = []
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

# driver.get("https://marketplace.akc.org/puppies?")
# time.sleep(3)
# search = driver.find_elements_by_class_name('sc-tilXH.cqzhjn')
#
# for element in search:
#     v = element.get_attribute('href')
#     data.append(v)
#
i = 3

while i < 855:
    driver.get("https://marketplace.akc.org/puppies?page={}".format(i))
    time.sleep(3)

    search = driver.find_elements_by_class_name('sc-tilXH.cqzhjn')
    for element in search:
        v = element.get_attribute('href')
        data.append(v)

    i += 1


with open('linksToLegitWebsites.csv', 'a') as linksToLegitWebsites:
    writer = csv.writer(linksToLegitWebsites, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(data)

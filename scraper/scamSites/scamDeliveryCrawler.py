import time
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

data = []

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')


def getwebsites(url):
    driver.get(url)
    time.sleep(3)

    localData = []

    websites1 = driver.find_elements_by_class_name('col-md-6.column-first')
    websites2 = driver.find_elements_by_class_name('col-md-6.column-second')

    websites = [websites1, websites2]

    for website in websites:
        for w in website:
            s = w.find_element_by_tag_name("h4").text
            s = s[0].lower() + s[1:]
            # s = link.get_attribute('href')
            s = "https://" + s
            data.append(s)

    # for w in websites2:
    #     link = w.find_element_by_tag_name("a")
    #     s = link.get_attribute('href')
    #     data.append(s)

    return localData


data.append(getwebsites("https://petscams.com/category/pet-delivery-agency/"))

i = 2

while i < 95:
    urlToPass = "https://petscams.com/category/pet-delivery-agency/page/{}/".format(i)
    data.append(getwebsites(urlToPass))
    i += 1



with open('scamDeliveryWebsites.csv', mode='w') as scamDeliveryWebsites:
    writer = csv.writer(scamDeliveryWebsites, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(data)


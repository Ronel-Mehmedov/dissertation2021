import time
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

data = []

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')


def getwebsites(url):
    driver.get(url)
    time.sleep(4)

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


data.append(getwebsites("https://petscams.com/category/puppy-scammer-list/"))

i = 2

while i < 205:
    urlToPass = "https://petscams.com/category/puppy-scammer-list/page/{}/".format(i)
    data.append(getwebsites(urlToPass))
    i += 1


# driver.get("https://petscams.com/category/puppy-scammer-list/")
#
# time.sleep(3)
#
# websites1 = driver.find_elements_by_class_name('col-md-6.column-first')
# websites2 = driver.find_elements_by_class_name('col-md-6.column-second')
#
# for w in websites1:
#     link = w.find_element_by_tag_name("a")
#     s = link.get_attribute('href')
#     data.append(s)
#
# for w in websites2:
#     link = w.find_element_by_tag_name("a")
#     s = link.get_attribute('href')
#     data.append(s)
#
# driver.get("https://petscams.com/category/puppy-scammer-list/page/2/")
#
# time.sleep(3)
#
# websites1 = driver.find_elements_by_class_name('col-md-6.column-first')
# websites2 = driver.find_elements_by_class_name('col-md-6.column-second')
#
# for w in websites1:
#     link = w.find_element_by_tag_name("a")
#     s = link.get_attribute('href')
#     data.append(s)
#
# for w in websites2:
#     link = w.find_element_by_tag_name("a")
#     s = link.get_attribute('href')
#     data.append(s)



with open('petscamWebsites.csv', mode='w') as petscamWebsites:
    writer = csv.writer(petscamWebsites, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(data)


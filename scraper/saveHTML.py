from selenium import webdriver

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

name = "https://www.ipata.org/ipata-pet-ground-transporters"

driver.get(name)
with open('/home/x/dissertation/data/downloadedHTML', 'w+') as f:
    f.write(driver.page_source)
    f.close()


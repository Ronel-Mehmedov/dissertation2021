import os
import csv

homeFolder = "/home/x/allDataBackup/scamDeliverers"
empties = []
for folder in os.scandir(homeFolder):
    folderPath = os.path.join(homeFolder, folder.name)
    dateFile = os.path.join(folderPath, "date")
    if not os.path.exists(dateFile):
        empties.append(folder.name)

emptiesCSV = os.path.join("/home/x/dissertation/scraper", "nonDatedScamSites.csv")
with open(emptiesCSV, 'w') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(empties)
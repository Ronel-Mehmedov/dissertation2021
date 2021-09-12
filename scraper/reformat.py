import csv

with open('/home/x/dissertation/scraper/scamSites/scamDeliverersToCrawl') as f:
    contents = f.read()
    wordList = contents.split('\n')
    print(len(wordList))

with open('/home/x/dissertation/scraper/scamSites/finalScamDeliverersToCrawl.csv', 'a') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(wordList)
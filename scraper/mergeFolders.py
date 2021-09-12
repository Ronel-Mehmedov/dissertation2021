import os
import shutil

main = []

added = []


for folder in os.scandir('/home/x/testFollow2'):
    added.append(folder.name)

for folder1 in os.scandir('/home/x/testFollow'):
    main.append(folder1.name)

for website in added:
    for entry in main:
        if website == entry:
            pathToDelete = os.path.join('/home/x/testFollow', website)
            print(pathToDelete)
            try:
                shutil.rmtree(pathToDelete)
            except OSError as e:
                print ("Error: %s - %s." % (e.filename, e.strerror))

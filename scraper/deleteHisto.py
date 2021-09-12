import os
import csv
import shutil

# with open('/home/x/histos/zero.csv') as csv_file1:
#     csv_reader = csv.reader(csv_file1, delimiter=',')
#     for row in csv_reader:
#         for entry in row:
#             pathToDelete = os.path.join('/home/x/followupDeliveryScam', entry)
#             try:
#                 shutil.rmtree(pathToDelete)
#             except OSError as e:
#                 print ("Error: %s - %s." % (e.filename, e.strerror))

for folder in os.scandir('/home/x/followupDeliveryScam'):
    if "1053" in folder.name:
        folderToDel = os.path.join('/home/x/followupDeliveryScam', folder.name)
        print(folderToDel)
        try:
            shutil.rmtree(folderToDel)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

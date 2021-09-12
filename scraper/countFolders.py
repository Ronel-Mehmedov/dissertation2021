import os

count = 0
for folder in os.scandir('/home/x/allDataBackup/scamDeliverers'):
    count += 1

print(count)

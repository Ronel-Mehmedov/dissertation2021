import csv

count = 0
with open('/home/x/allDataBackup/marketplace') as csv_file1:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        for entry in row:
            print(entry)
            count += 1

print(count)


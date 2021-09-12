import os
import csv

count = 0

with open('/home/x/histos/zero.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 0))
count = 0

with open('/home/x/histos/one.csv') as csv_file1:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 1))
count = 0

with open('/home/x/histos/two.csv') as csv_file2:
    csv_reader = csv.reader(csv_file2, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 2))
count = 0

with open('/home/x/histos/three.csv') as csv_file3:
    csv_reader = csv.reader(csv_file3, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 3))
count = 0

with open('/home/x/histos/four.csv') as csv_file4:
    csv_reader = csv.reader(csv_file4, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 4))
count = 0

with open('/home/x/histos/fiveToTen.csv') as csv_file510:
    csv_reader = csv.reader(csv_file510, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 5))
count = 0

with open('/home/x/histos/tens.csv') as csv_file10:
    csv_reader = csv.reader(csv_file10, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 10))
count = 0

with open('/home/x/histos/twenties.csv') as csv_file20:
    csv_reader = csv.reader(csv_file20, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 20))
count = 0

with open('/home/x/histos/thirties.csv') as csv_file30:
    csv_reader = csv.reader(csv_file30, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 30))
count = 0

with open('/home/x/histos/forties.csv') as csv_file40:
    csv_reader = csv.reader(csv_file40, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 40))
count = 0

with open('/home/x/histos/fiftys.csv') as csv_file50:
    csv_reader = csv.reader(csv_file50, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 50))
count = 0

with open('/home/x/histos/sixtys.csv') as csv_file60:
    csv_reader = csv.reader(csv_file60, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 60))
count = 0

with open('/home/x/histos/seventy.csv') as csv_file70:
    csv_reader = csv.reader(csv_file70, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 70))
count = 0

with open('/home/x/histos/hundred.csv') as csv_file100:
    csv_reader = csv.reader(csv_file100, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1

print("{} files with {} entries".format(count, 100))
count = 0
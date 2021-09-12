import csv

with open('/home/x/codesForScamDeliveryIMGS.csv') as csv_file1:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        if "bee0915ec299c94b" in row:
            print(row[0])


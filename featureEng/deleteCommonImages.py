import os
import csv
filteredList = []

bannedCodes = ["0000000000000000","8000000000000000", "bea0b965c0d9c19e", "9a6e656f24869e98", "bee0915ec299c94b"]

with open('/home/x/codesForScamDeliveryIMGS.csv') as csv_file1:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    for row in csv_reader:
        flag = True
        for item in row:
            for entry in bannedCodes:
                if entry == item:
                    flag = False
                    # print(row[0])
        if flag == True:
            filteredList.append(row)

targetCodes = []
count = 0
with open("/home/x/targetDeliveryHashCodes.csv") as csv_file2:
    # with open('./marketplace/mainMarketplaceList.csv') as csv_file:
    csv_reader = csv.reader(csv_file2, delimiter=',')
    for row in csv_reader:
        for entry in row:
            count += 1
            targetCodes.append(entry)

print(count)
finalList = []

count = 0
for targetCode in targetCodes:
    flag2 = True
    print("starting new targetCode - {}".format(targetCode))
    for websiteList in filteredList:
        print("checking website")
        for code in websiteList:
            if targetCode == code:
                finalList.append(websiteList[0])
                print("{} : {}".format(websiteList[0], code))
                filteredList.remove(websiteList)
                flag2 = False
                count += 1
                break
        if flag2 == False:
            break

print(count)
print(sorted(finalList))

with open("/home/x/referenceDeliverScamSites.csv", 'w') as b:
    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(finalList)

# def removeDuplicates(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if len(nums) == 0:
#         return 0
#     length = 1
#     previous = nums[0]
#     index = 1
#     for i in range(1,len(nums)):
#         if nums[i] != previous:
#             length += 1
#             previous = nums[i]
#             nums[index] = nums[i]
#             index+=1
#     return length
#
# removeDuplicates(finalList)

print(len(finalList))



import os
count = 0

for root, dirs, files in os.walk("/home/x/data", ):
    for name in files:
        fileName = os.path.join(root, name)
        if "%" in fileName:
            count += 1
            print(fileName)



print(count)

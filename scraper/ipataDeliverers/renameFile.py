import os

root = '/home/x/deliverers'

count = 0

for folder in os.scandir(root):
    initPath = os.path.join(root, folder.name)
    htmlPath = os.path.join(initPath, "HTML")
    for element in os.scandir(htmlPath):
        pathString = os.path.join(htmlPath, element.name)
        newName = pathString.replace('??', '!')
        os.rename(pathString, newName)
        count += 1

print(count)
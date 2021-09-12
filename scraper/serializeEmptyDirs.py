import os
import shutil


rootDir = "../data/"

empty = 0
notEmpty = 0
singleEntry = 0

for folder in os.scandir(rootDir):
    path = os.path.join(rootDir, folder.name)
    print(path)
    path = os.path.join(path, "HTML")
    size = os. listdir(path)
    length = len(size)
    print("{} contains {} files".format(folder.name, length))
    if length == 0:
        print("folder is empty")
        empty += 1
    elif length == 1:
        print("folder has a single entry")
        singleEntry += 1
    else:
        notEmpty += 1
    print("============================")


print("{} empty files".format(empty))

print("{} files are not empty".format(notEmpty))

print("{} files have a single entry".format(singleEntry))

# for subdir, dirs, files in os.walk(rootDir):


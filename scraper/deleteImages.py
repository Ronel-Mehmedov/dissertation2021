import os

rootDir = "/home/x/dissertation/data"

for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        if ".jpg" in file or ".jpeg" in file or ".mpeg" in file or ".gif" in file or ".png" in file:
            path = os.path.join(subdir, file)
            os.remove(path)
            print("removed {}".format(path))

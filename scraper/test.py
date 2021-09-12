import os

for folder in os.scandir("../test/Enviziondogs.com/HTML"):
    print(folder.name)
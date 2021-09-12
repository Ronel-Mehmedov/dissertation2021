import os

banList = ["facebook", "twitter", "youtube", "pinterest", "instagram", "google", "linkedin", "#", "?", ".jpg", ".jpeg", ".mpeg", ".png", ".gif", ".pdf", "archive", "copy", "attachment"]

deleted = 0


def correct(filePath):
    if not freeOfJunk(filePath):
        return False
    # if lenDif > 38:
    #     return False
    if not validHTML(filePath):
        return False
    return True

def validHTML(filePath):
    if os.path.exists(filePath):
        checkfile=open(filePath, mode="r", encoding="utf-8")
    ishtml = False
    try:
        for line in checkfile:
            line=line.strip()
            if "<html" in line:
                ishtml = True
    except:
        print(filePath + " - error: could not read to validate HTML")
    if ishtml:
        return True
    else:
        return False




def freeOfJunk(filePath):
    for entry in banList:
        if entry in filePath.lower():
            return False
    return True


for folder in os.scandir('/home/x/deliverers'):
    initPath = os.path.join('/home/x/deliverers', folder.name)
    htmlPath = os.path.join(initPath, "HTML")
    for file in os.scandir(htmlPath):
        pathOfFile = os.path.join(htmlPath, file.name)
        boolFlag = correct(pathOfFile)
        if not boolFlag:
            if os.path.exists(pathOfFile):
                os.remove(pathOfFile)
                print(pathOfFile)
                deleted += 1

            else:
                print("The file does not exist")


print(deleted)
        
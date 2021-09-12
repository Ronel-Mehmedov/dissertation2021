import os
from bs4 import BeautifulSoup as bs
import re


searchWords = ['contact', 'about']
count = 0
def wrapper(text):
    response = text.replace("\n", "")
    response = response.replace("\t", "")
    response = response.replace("", "")
    response = ' '.join(response.split())
    if len(response) > 40:
        return ""
    return response


def getSiblings(scores):
    liList = []
    for i in scores.previous_siblings:
        if i.name == 'li':
            liList.append(i)
    liList.append(scores)
    for i in scores.next_siblings:
        if i.name == 'li':
            liList.append(i)
    return liList

def extractFromLI(liTag):
    textChildren = []
    children = liTag.findChildren(recursive=True)
    for child in children:
        if child.name == 'a' and hasattr(child, 'text'):
            label = wrapper(child.text)
            if label not in textChildren and label != "":
                textChildren.append(label)
    return textChildren


# def getChild(tag):
#     children = tag.findChildren(recursive=True)
#     for child in children:
#         if hasattr(child, "text"):
#             if "home" in child.text.lower():
#                 return True
#     return False

def getChildLIS(tag):
    children = tag.findChildren(recursive=True)
    for child in children:
        if hasattr(child, "text"):
            for word in searchWords:
                if word in child.text.lower():
                    return True
    return False

def extractTextFromLI(tag):
    textChildren = []
    children = tag.findChildren(recursive=True)
    for child in children:
        if child.name == 'a':
            grandChildren = child.findChildren(recursive=True)
            if len(grandChildren) > 0:
                for grandChild in grandChildren:
                    if hasattr(grandChild, 'text'):
                        label = wrapper(grandChild.text)
                        if label not in textChildren and label != "":
                            textChildren.append(label)
            else:
                if hasattr(child, 'text'):
                    label = wrapper(child.text)
                    if label not in textChildren and label != "":
                        textChildren.append(label)
    return textChildren




def tryLIS(soup):
    LIS = soup.findAll('li')
    optionsMenu = []
    lis = None
    for li in LIS:
        if getChildLIS(li) is True:
            lis = getSiblings(li)
            break
    if lis is not None:
        for liTag in lis:
            for textFromTag in extractTextFromLI(liTag):
                label = wrapper(textFromTag).lower()
                if label not in optionsMenu and label != "":
                    optionsMenu.append(label)
    return optionsMenu


# def tryLIS(soup):
#     homeSpan = soup.find('li', text=re.compile('home', flags=re.IGNORECASE), recursive=True)
#     if homeSpan is None or len(homeSpan) == 0:
#         print(folder)
#     elif (len(homeSpan) > 0):
#         global count
#         count += 1

def navtagFind(soup):
    navTag = soup.find('nav')
    textChildren = []
    if navTag is not None:
        children = navTag.findChildren(recursive=True)
        for child in children:
            if child.name == 'a':
                grandChildren = child.findChildren(recursive=True)
                if len(grandChildren) > 0:
                    for grandChild in grandChildren:
                        if hasattr(grandChild, 'text'):
                            label = wrapper(grandChild.text).lower()
                            if label not in textChildren and label != "":
                                textChildren.append(label)
                else:
                    if hasattr(child, 'text'):
                        label = wrapper(child.text).lower()
                        if label not in textChildren and label != "":
                            textChildren.append(label)

    return textChildren

# def navtagFind(soup):
#     navTag = soup.find('nav')
#     if navTag is not None:
#         children = navTag.findChildren(recursive=True)
#         for child in children:
#             if child.name == 'a' and hasattr(child, 'text') and ("contact" in child.text or "about in child.text"):
#                 return getSiblings(child)
#     return []

def resolveUnloaded(filePath):
    options = []
    try:
        text = open(filePath, 'r').read()
    except:
        return []
    result = re.findall('"title":"[^"]*"', text)
    for i in result:
        label = wrapper(i.split('\"')[3]).lower()
        if label not in options and label != "":
            options.append(label)
    return options


# def tryAll(soup):
#     tags = soup.findAll()
#     for tag in tags:
#         flag, tagVal = getChildLIS(tag)
#         if flag == True:
#             return getSiblings(tagVal)
#     return []

def tryAll(soup):
    # tags = soup.findAll()
    # for tag in tags:
    #     flag, tagVal = getChildLIS(tag)
    #     if flag == True:
    #         return getSiblings(tagVal)
    return []


root = '/home/x/specialty/marketplace'

index = {}
count = 0
for folder in os.listdir('/home/x/specialty/marketplace'):
    menuOptions = []
    folderPath = os.path.join(root, folder)
    folderPath = folderPath + '/HTML'
    shortest = min(os.listdir(folderPath), key=len)
    filePath = os.path.join(folderPath, shortest)
    soup = bs(open(filePath, 'rb'), "html.parser")
    options = navtagFind(soup)
    if len(options) > 0:
        index[folder] = options
        count += 1
        print("{}: nav - {}".format(folder, options))
    else:
        options = tryLIS(soup)
        if len(options) > 0:
            index[folder] = options
            count += 1
            print("{}: tryLIS - {}".format(folder, options))
        else:
            options = tryAll(soup)
            if len(options) > 0:
                index[folder] = options
                count += 1
                print("{}: tryAll - {}".format(folder, options))
            else:
                options = resolveUnloaded(filePath)
                if len(options) > 0:
                    count += 1
                    index[folder] = options
                    print("{}: resolveUnloaded - {}".format(folder, options))
                else:
                    print("faulty: {}".format(folder))


print(count)





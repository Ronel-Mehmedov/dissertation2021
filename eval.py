import os
from bs4 import BeautifulSoup as bs
import bs4
import re

bannedPool = ['home', 'available', 'about', 'shipping', 'shipment', 'delivery', 'polic', 'guarantee', 'condition', 'payment', 'testimon', 'review', 'reach', 'touch', 'faq', 'services', 'welcome']
searchWords = ['home', 'about us', 'about', 'contact', 'contact us', 'welcome', 'reach us', 'zuhause', 'startseite', 'pagrindinis', 'accueil']
count = 0
def wrapper(text):
    response = text.text
    response = response.replace("\n", "")
    response = response.replace("\t", "")
    response = response.replace("", "")
    response = ' '.join(response.split())
    response = response.strip()
    response = response.lower()
    if len(response) > 40:
        return ""
    return response

def wrapper2(text):
    response = text.replace("\n", "")
    response = response.replace("\t", "")
    response = ' '.join(response.split())
    response = response.strip()
    if len(response) > 40:
        return ""
    return response


def countOccurances(inputList):
    count = 0
    for word in inputList:
        for ban in bannedPool:
            if ban in word:
                count += 1
                break
    return float(count) / float(len(inputList))



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

def getSiblings2(scores):
    liList = []
    for i in scores.previous_siblings:
        if not isinstance(i, bs4.element.NavigableString):
            liList.append(i)
    liList.append(scores)
    for i in scores.next_siblings:
        if not isinstance(i, bs4.element.NavigableString):
            liList.append(i)
    return liList

def probe(parent, depth):
    if depth == 7:
        return False, [], depth
    siblings = getSiblings2(parent)
    lenOfSiblings = len(siblings)
    lenOfAs = 0
    toRemove = []
    for i in range(lenOfSiblings):
        if hasAtag(siblings[i], depth) == True:
            lenOfAs += 1
        else:
            toRemove.append(siblings[i])
    for index in toRemove:
        siblings.remove(index)
    if lenOfAs == len(siblings):
        return True, siblings, depth
    return probe(parent.parent, depth + 1)

def locateHome(soup):
    answer = []
    aTags = soup.findAll('a')
    for aTag in aTags:
        if hasattr(aTag, 'text') and hasattr(aTag, 'href'):
            compWord = wrapper2(aTag.text.lower())
            for word in searchWords:
                if word == compWord:
                    answer.append(aTag)
        children = aTag.findChildren(recursive=True)
        for child in children:
            if hasattr(child, "text"):
                for word in searchWords:
                    if word == wrapper2(child.text.lower()):
                        answer.append(aTag)
    return answer

def driver(soup):
    homeTag = locateHome(soup)
    if len(homeTag) == 0:
        return []
    for aTag in homeTag:
        flag, siblingsList, depth = probe(aTag.parent, 1)
        if flag == True:
            text = collectText(siblingsList, depth)
            lenNum = 0
            for element in text:
                if element != '' and sanitize(element) == True and '@' not in element:
                    lenNum += 1
            if lenNum > 2:
                return text
    return []

def sanitize(input):
    count1 = 0
    for i in input:
        if(i.isdigit()):
            count1=count1+1
        if count1 > len(input):
            return False
        else:
            return True


def hasAtag(parentTag, depth):
    answer = []
    currQue = parentTag.findChildren()
    resQue = []

    for i in range(depth -1):
        for tag in currQue:
            for subTag in tag.findChildren():
                resQue.append(subTag)
        currQue = resQue
        resQue = []

    for tag in currQue:
        if tag.name == 'a':
            return True
    return False



def collectAs(parentTag, depth):
    answer = []
    currQue = parentTag.findChildren()
    resQue = []

    for i in range(depth - 1):
        for tag in currQue:
            for subTag in tag.findChildren():
                resQue.append(subTag)
        currQue = resQue
        resQue = []

    for tag in currQue:
        if tag.name == 'a':
            return tag


    # children = tag.findChildren(recursive=True)
    # for child in children:
    #     if child.name == 'a':
    #         return True
    # return False

def collectText(siblings, depth):
    menuOptions = []
    for sibling in siblings:
        response = wrapper(collectAs(sibling, depth))
        if response != '':
            menuOptions.append(response)
    return menuOptions



root = '/home/x/specialty/scamSites'

map = {}
count = 0
for folder in os.listdir('/home/x/specialty/scamSites'):
    menuOptions = []
    folderPath = os.path.join(root, folder)
    folderPath = folderPath + '/HTML'
    shortest = min(os.listdir(folderPath), key=len)
    filePath = os.path.join(folderPath, shortest)
    soup = bs(open(filePath, 'rb'), "html.parser")
    options = driver(soup)
    if len (options) > 0:
        #
        # print("{} - {}".format(folder, options))
        if countOccurances(options) >= 0.85:
            count += 1
        # for option in options:
        #     if option in map.keys():
        #         map[option] += 1
        #     else:
        #         map[option] = 1

print(count)
# for key in dict(sorted(map.items(), key=lambda item: item[1])).keys():
#     print("{} : {}".format(key, map[key]))

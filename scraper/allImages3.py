import csv

import requests
import os
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse




homeFolder = "/home/x/allDataBackup/marketplace"

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(path, url):
    """
    Returns all image URLs on a single `url`
    """
    urls = []
    try:
        soup = bs(open(path, encoding="utf8"), "html.parser")
    except:
        return urls



    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        try:
            img_url = urljoin(url, img_url)
        except:
            pass
        #
        # # make the URL absolute by joining domain with the URL that is just extracted
        # try:
        #     pos = img_url.index("?")
        #     img_url = img_url[:pos]
        # except ValueError:
        #     pass


        # finally, if the url is valid
        if is_valid(img_url):
            urls.append(img_url)

    for img in soup.find_all("a"):
        img_url = img.attrs.get("href")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        img_url = urljoin(url, img_url)
        #
        # # make the URL absolute by joining domain with the URL that is just extracted
        # try:
        #     pos = img_url.index("?")
        #     img_url = img_url[:pos]
        # except ValueError:
        #     pass


        # finally, if the url is valid
        if is_valid(img_url) and (".jpeg" in img_url or ".jpg" in img_url or ".png" in img_url):
            urls.append(img_url)

    return urls

def download(url, pathname, session, counter):
    # print("downloading {}".format(url))
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    try:
        response = session.get(url, stream=True, timeout=10)
        # get the total file size
        file_size = int(response.headers.get("Content-Length", 0))
        # get the file name
        filename1 = "image" + str(counter)
        filename = os.path.join(pathname, filename1)
        # progress bar, changing the unit to bytes instead of iteration (default by tqdm)

        with open(filename, "wb") as f:
            for data in response.iter_content(1024):
                # write data read to the file
                f.write(data)
    except:
        # print("failed to get url: {}".format(url))
        pass



def main():
    websittesList = []

    with open('/home/x/dissertation/scraper/marketplace/finalListToCrawl.csv') as csv_file1:
        csv_reader = csv.reader(csv_file1, delimiter=',')
        for row in csv_reader:
            for entry in row:
                websittesList.append(entry)

    # get all images
    session = requests.Session()
    for folder in os.scandir(homeFolder):

        mode = 0o755
        initPath = os.path.join(homeFolder, folder.name)
        htmlPath = os.path.join(initPath, "HTML")
        imagesFolderPath = os.path.join(initPath, "Images")
        print("checking if {} exists".format(imagesFolderPath))
        if not os.path.exists(imagesFolderPath):
            print("does not exist")
            try:
                os.mkdir(imagesFolderPath, mode)
            except:
                pass


            searchName = folder.name.lower()
            searchName = searchName.replace("https://", "")
            searchName = searchName.replace("http://", "")
            searchName = searchName.replace("www.", "")
            websiteName = ''
            foundFlag = False

            for website in websittesList:
                if searchName in website:
                    websiteName = website
                    foundFlag = True

            if foundFlag is True:
                try:
                    req = session.get(websiteName, timeout=10)
                    url = req.url
                except:
                    pass



                allImgs = []
                for item in os.scandir(htmlPath):

                    htmlFileName = os.path.join(htmlPath, item.name)
                    # path = os.path.join("../legitDeliverers/nanissen.dk/HTML", item.name)
                    imgs = get_all_images(htmlFileName, url)
                    for entry in imgs:
                        if entry not in allImgs:
                            allImgs.append(entry)
                print("images are:")
                print(allImgs)
                counter = 0
                for img in allImgs:
                    counter += 1
                    download(img, imagesFolderPath, session, counter)
                logPath = os.path.join(initPath, "imageSources.csv")
                with open(logPath, 'a') as b:
                    writer = csv.writer(b, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(allImgs)


main()
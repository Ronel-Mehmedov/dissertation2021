import requests
import os
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    soup = bs(open("../legitDeliverers/nanissen.dk/HTML/main", encoding="utf8"), "html.parser")


    urls = []
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue

        # make the URL absolute by joining domain with the URL that is just extracted
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass


        # finally, if the url is valid
        if is_valid(img_url):
            urls.append(img_url)
    return urls

def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)

    with open(filename, "wb") as f:
        for data in response.iter_content(1024):
            # write data read to the file
            f.write(data)



def main(url, path):
    # get all images
    imgs = get_all_images(url)
    for img in imgs:
        # for each image, download it
        download(img, path)


main("https://nanissen.dk", "yandex-images")


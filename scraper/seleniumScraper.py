import time

from requests_html import HTMLSession
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



# based on code from https://www.thepythoncode.com/code/extract-all-website-links-python

# init the colorama module
colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW

# initialize the set of links (unique links)
visited = set()
internal_urls = set()
external_urls = set()

total_urls_visited = 0

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')



def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url, session):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """

    # all URLs of `url`
    urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc.replace("www.", "")
    print("domain name is {}".format(domain_name))
    # initialize an HTTP session

    sessionInitialised = True

    try:
        driver.get(url)
    except Exception as E:
        sessionInitialised = False
        print(E)
        traceback.print_exc()
        pass

    if sessionInitialised == True:
        elem = driver.find_elements_by_tag_name("a")
        for a_tag in elem:
            href = a_tag.get_attribute("href")
            if href == "" or href is None:
                # href empty tag
                continue
            # join the URL if it's relative (not absolute link)
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            # remove URL GET parameters, URL fragments, etc.
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not is_valid(href):
                # not a valid URL
                continue
            if href in internal_urls:
                # already in the set
                continue
            if domain_name not in href:
                # external link
                if href not in external_urls:
                    print(f"{GRAY}[!] External link: {href}{RESET}")
                    external_urls.add(href)
                continue
            if ' ' not in href and "facebook" not in href and "twitter" not in href and "youtube" not in href and "pinterest" not in href and "instagram" not in href and "google" not in href and "linkedin" not in href and "#" not in href and "?" not in href and ".jpg" not in href and ".jpeg" not in href and ".mpeg" not in href and ".png" not in href and ".gif" not in href and ".pdf" not in href and "archive" not in href and "copy" not in href and "attachment" not in href and "@" not in href:
                print(f"{GREEN}[*] Internal link: {href}{RESET}")
                urls.add(href)
                internal_urls.add(href)
                print(internal_urls)
            session.close()
        return urls



def crawl(url, session, max_urls=200):
    """
    Crawls a web page and extracts all links.
    You'll find all links in `external_urls` and `internal_urls` global set variables.
    params:
        max_urls (int): number of max urls to crawl, default is 30.
    """
    global total_urls_visited
    total_urls_visited += 1
    print(f"{YELLOW}[*] Crawling: {url}{RESET}")


    links = get_all_website_links(url, session)

    visited.add(url)
    if links is not None:
        for link in links:
            if link not in visited:
                if total_urls_visited > max_urls:
                    print("max urls number reached")
                    break
                crawl(link, session, max_urls=max_urls)


def execute(url):
    session = HTMLSession()
    req = requests.get(url)
    headers = req.headers
    url = req.url

    crawl(url, session)
    return internal_urls, external_urls, headers
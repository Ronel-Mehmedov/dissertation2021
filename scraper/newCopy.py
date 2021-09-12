from requests_html import HTMLSession
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama
import os

# based on code from https://www.thepythoncode.com/code/extract-all-website-links-python


# initialize the set of links (unique links)
visited = set()
internal_urls = set()

total_urls_visited = 0


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """

    if url in visited:
        return None

    # all URLs of `url`
    urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    # initialize an HTTP session

    sessionInitialised = True

    try:
        session = HTMLSession()
        # make HTTP request & retrieve response
        response = session.get(url)
        # execute Javascript
        response.html.render()
    except:
        sessionInitialised = False
        pass

    if sessionInitialised == True:
        visited.add(url)
        soup = BeautifulSoup(response.html.html, "html.parser")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
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
                continue

            if href not in visited and href not in internal_urls:
                # print("[*] Internal link: {}".format(href))
                internal_urls.add(href)
                urls.add(href)
            session.close()
        return urls



def crawl(url, max_urls=30):
    """
    Crawls a web page and extracts all links.
    You'll find all links in `external_urls` and `internal_urls` global set variables.
    params:
        max_urls (int): number of max urls to crawl, default is 30.
    """
    global total_urls_visited
    total_urls_visited += 1
    print("[*] Crawling: {}".format(url))



    links = get_all_website_links(url)

    visited.add(url)
    if links is not None:
        for link in links:
            if link not in visited:
                if total_urls_visited > max_urls:
                    print("max urls number reached")
                    break
                crawl(link, max_urls=max_urls)


def execute(url):
    crawl(url)
    return internal_urls

# def createLeafDir(mainWebsite, innerLink, pathParent):
#     leafName = innerLink.split(mainWebsite)[-1]
#     leafName = leafName.replace("/", "??")
#     if leafName == "":
#         leafName = "main"
#     leafPath = os.path.join(pathParent, leafName)
#     mode = 0o755
#     os.mkdir(leafPath, mode)
#     return leafPath
#

import urllib.request

def get_html(url):
    f=open("/home/x/dissertation/data/downloadedHTML",'wb')
    page=urllib.request.urlopen(url)
    pagetext=page.read()
    f.write(pagetext)
    f.close()

get_html("https://www.ipata.org/ipata-pet-ground-transporters")
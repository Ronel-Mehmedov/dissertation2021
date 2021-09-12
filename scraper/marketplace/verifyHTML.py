import os
from bs4 import BeautifulSoup
import sys




rootDir = "/home/x/sss/www.amwat.com.mx/index.html"

if os.path.exists(rootDir):
    checkfile=open(rootDir, mode="r", encoding="utf-8")
    ishtml = False
    for line in checkfile:
        line=line.strip()
        if "</html>" in line:
            ishtml = True
    if ishtml:
        print("This is an html file")
    else:
        print("This is not an html file")

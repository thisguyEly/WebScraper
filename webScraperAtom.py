# Pandas for converting resultset to csv
import pandas as pd
import scipy as sy
import pytesseract as pt
import scrapy.crawler
import scrapy

# BeautifulSoup for scraping html in sites
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

# 1st reference site = featoflouisville
url = "https://featoflouisville.org/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# start scrapes
def scrape():
    for i in links:

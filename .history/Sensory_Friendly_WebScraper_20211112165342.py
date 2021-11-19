import requests
import csv
import re
import random
from bs4 import BeautifulSoup
import time
from urllib.request import Request, urlopen

# Open webpage
url = "https://featoflouisville.org/calendar/"
response = requests.get(url)
page = urlopen(url).read()

web_byte = urlopen(response).read()

webpage = web_byte.decode('utf-8')
#req = Request("https://featoflouisville.org/calendar/", headers={'User-Agent': 'XYZ/3.0'})
#webpage = urlopen(req, timeout=10).read()

soup = BeautifulSoup(req.text, "html.parser")
soup.findAll('a')

html_bytes = page.read()
html = html_bytes.decode("utf-8")

# pull sensory friendly events 
pattern = "<title.*?>.*?</title.*?>"
txt = "sensory"
match_results = re.search(r"\bS\w+",txt,re.IGNORECASE)
title = match_results.group()

# print(match_results.group())

pages = []

txt = "sensory"
x = re.search(r"\bs\w+", txt)
# print(x.group())

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    last_links = soup.find('table', attrs={'class': 'resultsTable'})

# create csv file for results
f = csv.writer(open('Sensory_Friendly_Events.csv', 'w'))
f.writerow(['Event Title ' , ' Link']) 

title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")

title = html[start_index:end_index]
title

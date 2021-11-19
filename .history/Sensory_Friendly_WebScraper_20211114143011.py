import os
import requests
import csv
import re
import random
#from bs4 import BeautifulSoup
import time
from urllib.request import Request, urlopen

# Open webpage
url = "https://www.amctheatres.com/programs/sensory-friendly-films"
req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

web_byte = urlopen(req, timeout=15).read()
webpage = web_byte.decode('utf-8')


#soup = BeautifulSoup(req.text, "html.parser")
#soup.findAll('a')

#html_bytes = webpage.read()
#html = html_bytes.decode("utf-8")

# pull sensory friendly events 
pattern = "<title.*?>.*?</title.*?>"
txt = "sensory"
match_results = re.search(r"\bS\w+",txt,re.IGNORECASE)
title = match_results.group()

print(match_results.group())

pages = []

txt = "sensory"
x = re.search(r"\bs\w+", txt)
print(x.group())

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    last_links = soup.find('table', attrs={'class': 'resultsTable'})

# create csv file for results
f = csv.writer(open('Sensory_Friendly_Events.csv', 'w'))
f.writerow(['Event Title ' , ' Link']) 

title_index = webpage.find("<title>")
start_index = title_index + len("<title>")
end_index = webpage.find("</title>")

title = webpage[start_index:end_index]
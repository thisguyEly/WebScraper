import requests
import csv
import re
from bs4 import BeautifulSoup
import time
from urllib.request import Request, urlopen

# Open webpage
url = requests.get("https://www.amctheatres.com/programs/sensory-friendly-films")
soup = BeautifulSoup(url.content,'html.parser')

#CSV File
filename = "Sensory Friendly Events.csv"
csv_writer = csv.writer(open(filename,'w'))

#soup = BeautifulSoup(req.text, "html.parser")
#soup.findAll('a')

#html_bytes = webpage.read()
#html = html_bytes.decode("utf-8")

# pull sensory friendly events 

for item in soup.pages(""):
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
from urllib3 import urllib3
import csv
from requests import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.amctheatres.com/programs/sensory-friendly-films'
resp = urllib3.request(url, headers={
                          'User-Agent': 'Mozilla/5.0 (Windows  NT 10.0; Win64; x64; rv:66.0) Firefox/66.0'}, redirect=False,timeout=4.0)
page = urllib3.urlopen(resp)
soup = BeautifulSoup(page, 'html.parser')

rows = soup.find('div' '_class=PosterContent').find(
    'span class="MoviePosters__released-month clearfix')

# Create CSV File
file = open('Sensory_Friendly_Showtimes.csv', 'wb')
writer = csv.writer(file)

# CSV Header Rows
writer.writerows({'Title', 'Date'})

for row in rows:
    title = row.find('a').text.strip()
    date = row.find('b').text.strip()

    print(title + ' ' + date)
    writer.writerows({title.encode('utf-8'), date.encode('utf-8')})

file.close()

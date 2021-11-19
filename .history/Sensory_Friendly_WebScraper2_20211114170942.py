from os import write
import urllib3
import csv
from bs4 import BeautifulSoup 

url = "https://www.amctheatres.com/programs/sensory-friendly-films"
request = urllib3.request(url,headers={'User-Agent': 'Mozilla/5.0 (Windows  NT 10.0; Win64; x64; rv:66.0) Firefox/66.0'});
page = urllib3.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')

rows = soup.find('div', attrs={'style':'float: right; width:900px;'}).find_all('div', recursive = False)[4:]

# Create CSV File
file = open('Sensory_Friendly_Showtimes.csv','wb')
writer = csv.writer(file)

# CSV Header Rows
writer.writerows({'Title','Date'})

for row in rows:
    title = row.find('a').text.strip()
    date = row.find('b').text.strip()

    print(title + ' ' + date)
    writer.writerows({title.encode('utf-8'), date.encode('utf-8')})

file.close()
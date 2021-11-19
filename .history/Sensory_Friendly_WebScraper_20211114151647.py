import requests
import csv
#import pandas
import re
from bs4 import BeautifulSoup
import time
#from urllib.request import Request, urlopen

# Open webpage
url = requests.get("https://www.amctheatres.com/programs/sensory-friendly-films")
soup = BeautifulSoup(url.content,'html.parser')

#CSV File
filename = "Sensory_Friendly_Events.csv"
csv_writer = csv.writer(open(filename,'w'))

#soup = BeautifulSoup(req.text, "html.parser")
#soup.findAll('a')

#html_bytes = webpage.read()
#html = html_bytes.decode("utf-8")

# pull sensory friendly events 
for i in soup.find_all("sensory"):
    data = []

    for f in i.find_all("sensory"):
        data.append(i.text)
    if data:
        print("inserting headers : {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue

    for r in i.find_all("sensory"):
        if r.a:
            data.append(r.a.text.strip())
        else:
            data.append(r.text.strip())
    if data:
        print("inserting data: {}".format(','.join(data)))
        csv_writer.writerow(data)

#save csv file
filename.to_csv('Sensory_Friendly_Events.csv')
data.close()
import requests
import urllib.parse; urllib.request.http.client
import csv
import pandas as pd
import lxml
#import re
from bs4 import BeautifulSoup
#import time

# Open webpage
#url = requests.get("https://www.amctheatres.com/programs/sensory-friendly-films")
#soup = BeautifulSoup(url.content,'html.parser')

data = []
movie = []  

# Pull movie date & times
def main(): 
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.37"
    URL = "https://www.amctheatres.com/programs/sensory-friendly-films"
    response = requests.get(URL, headers={'User-Agent': user_agent})
    html = response.content

    soup = BeautifulSoup(html,"lxml")    
    print(soup.contents)

    i = 0

    for h3 in soup.find_all [i] ('div' 'class=Slide','h3'):
        movie.append(h3.get_text(strip=True))
        data.append(movie)
    for span in soup.find_all [i] ('span', 'class=MoviePosters__released-month clearfix'):
        movie.append(span.get_text(strip=True))
        data.append(movie)
        break
    i += 1
main()

#CSV File
df = pd.DataFrame(data, columns={"MovieTitle","ShowTime"})
df.to_csv('sensory_friendly_movies.csv', encoding='utf-8-sig', index = False)

#html_bytes = webpage.read()
#html = html_bytes.decode("utf-8")

#save csv file
#filename.close()
#filename.to_csv('Sensory_Friendly_Events.csv')
#data.close()
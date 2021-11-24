from bs4 import BeautifulSoup
import lxml
import pandas as pd
import csv
import requests
import urllib.parse
urllib.request.http.client
#import re
#import time

# Open webpage
#url = requests.get("https://www.amctheatres.com/programs/sensory-friendly-films")
#soup = BeautifulSoup(url.content,'html.parser')

#creating a list to retrieve values for movie dates
data = []
movie = []

# Building a web scraper topPull movie date from the AMC site. 

def main():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.37"
    URL = "https://www.amctheatres.com/programs/sensory-friendly-films"
    response = requests.get(URL, headers={'User-Agent': user_agent})
    html = response.content

    soup = BeautifulSoup(html, "lxml")
    print(soup.contents)

    for h3 in soup.find_all('div', attrs={'class': 'Slide'}):
        movie.append(h3.get_text(strip=True))
        data.append(movie)
    for span in soup.find_all('span', 'class=MoviePosters__released-month clearfix'):
        movie.append(span.get_text(strip=True))
        break

main()

# CSV File - Writing scraped movie into into a csv for user access
df = pd.DataFrame(data, columns={"MovieTitle",
                                 "ShowTime"})
df.to_csv('sensory_friendly_movies.csv', encoding='utf-8-sig', index=False)

# Requirement - Data visualization - Countdown (days) to event date
# Shows how many days are left till showtime - user simply needs to update current date

from datetime import date
current_date = date(2021, 11, 24)
end_date = date(2021, 11, 27)
delta = end_date - current_date
print(delta.days)


#html_bytes = webpage.read()
#html = html_bytes.decode("utf-8")

# save csv file
# filename.close()
# filename.to_csv('Sensory_Friendly_Events.csv')
# data.close()
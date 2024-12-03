from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Downloading imdb top 250 movie's data
url = 'https://www.imdb.com/chart/top/'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 " \
             "Safari/537.36 "
headers = {'User-Agent': user_agent}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

movies_list = []
for movie in soup.findAll('div', attrs={'class': 'sc-300a8231-0 gTnHyA cli-children'}):
    film = {'title': movie.findNext('h3').text.split(' ', 1)[1],
            'rank': movie.findNext('h3').text.split('.', 1)[0],
            'date': movie.findNext('span', attrs={'class': 'sc-300a8231-7 eaXxft cli-title-metadata-item'}).text,
            'duration': movie.find('div', class_='sc-300a8231-6 dBUjvq cli-title-metadata').find_all('span')[1].text,
            'rating': movie.findNext('span', attrs={'class': 'ipc-rating-star--rating'}).text}
    movies_list.append(film)

print(movies_list)

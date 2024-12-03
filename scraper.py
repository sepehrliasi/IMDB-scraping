from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Downloading imdb top 250 movie's data
url = 'https://www.imdb.com/chart/top/'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
# print(response.content)
# soup = BeautifulSoup(response.content, 'html5lib')
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

movies_list = []
table = soup.find('li', attrs={'class': 'ipc-metadata-list-summary-item sc-4929eaf6-0 DLYcv cli-parent'})
# print(table.prettify())
for row in table.find('div', attrs={'class': 'sc-300a8231-0 gTnHyA cli-children'}):
    movies = {}
    movies['title'] = row.find('h3', class_='ipc-title__text').text
    print(movies)
    # print(row.prettify())

movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
		for b in soup.select('td.posterColumn span[name=ir]')]

# create an empty list for storing
# movie information
list = []

# Iterating over movies to extract
# each movie's details
for index in range(0, len(movies)):
    # Separating movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index)) - (len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            "star_cast": crew[index],
            }
    list.append(data)

print(list)
for movie in list:
	print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
		') -', 'Starring:', movie['star_cast'], movie['rating'])


import requests
from bs4 import BeautifulSoup
import pandas as pd

s = int(input("press 1 for movies, 2 for TV series"))
r = ""

if s == 2:
	r = "tv/"

response = requests.get("http://www.imdb.com/chart/top"+r)
soup = BeautifulSoup(response.content, 'html.parser')

titlesls = []
movies_class = soup.find_all('td', class_='titleColumn')
for movie in movies_class:
    movie_name = movie.find('a').get_text()
    titlesls.append(movie_name)

yearsls = []
for movie in movies_class:
    year = movie.find('span').get_text()
    yr = year[1:5]
    yr = int(yr)
    yearsls.append(yr)

ratingsls = []
ratings = soup.find_all('td', class_ = 'ratingColumn imdbRating')
for rating in ratings:
    r = rating.find('strong').get_text()
    r = float(r)
    ratingsls.append(r) 

Data = list(zip(titlesls,yearsls,ratingsls))
df = pd.DataFrame(data = Data, columns=['Name', 'Year of release','Rating'])

if s == 1:
	df.to_csv('top-250-movies.csv',index=False,header=False)
else:
	df.to_csv('top-250-series.csv',index=False,header=False)		





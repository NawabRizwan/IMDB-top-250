import requests
from bs4 import BeautifulSoup
import pandas as pd

#get user input for donwloading list of movies or TV series
s = int(input("press 1 for movies, 2 for TV series:	"))
r = ""

if s!=1 and s!=2:
	print("Wrong input, exiting")
	exit()

#If user selects TV series append the following text in the link
if s == 2:
	r = "tv/"


response = requests.get("http://www.imdb.com/chart/top"+r)
soup = BeautifulSoup(response.content, 'html.parser')

#get the titles of the movies or TV series and store in titlesls
titlesls = []
movies_class = soup.find_all('td', class_='titleColumn')
for movie in movies_class:
    movie_name = movie.find('a').get_text()
    titlesls.append(movie_name)

#get the year of release of the movies or TV series and store in yearsls
yearsls = []
for movie in movies_class:
    year = movie.find('span').get_text()
    yr = year[1:5]
    yr = int(yr)
    yearsls.append(yr)

#get the ratings of the movies or TV series and store in ratingsls
ratingsls = []
ratings = soup.find_all('td', class_ = 'ratingColumn imdbRating')
for rating in ratings:
    r = rating.find('strong').get_text()
    r = float(r)
    ratingsls.append(r) 

#zip all the data in a list
Data = list(zip(titlesls,yearsls,ratingsls))
df = pd.DataFrame(data = Data, columns=['Name', 'Year of release','Rating'])

#store the .csv file
if s == 1:
	df.to_csv('top-250-movies.csv',index=False,header=True)
else:
	df.to_csv('top-250-series.csv',index=False,header=True)		





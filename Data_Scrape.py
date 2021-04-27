

import pandas as pd
import requests
from bs4 import BeautifulSoup

page=requests.get('http://www.imdb.com/chart/top')

soup=BeautifulSoup(page.text,'lxml')
soup.title.text


movies=soup.select('td.titleColumn')
year=soup.select('span.secondaryInfo')
rating=soup.select('td.ratingColumn.imdbRating strong')


movies[150].a.text

year[150].text

rating[150].text

Name=[]
Releaseyear=[]
Rating=[]

for i in range(0, len(movies)):
    Name.append(movies[i].a.text)
    Releaseyear.append(year[i].text)
    Rating.append(rating[i].text)


data=list(zip(Name,Releaseyear,Rating))

df=pd.DataFrame(data,columns=['Name','Year','Rating'])

df


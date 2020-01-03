import bs4
import pandas as pd
import requests

url = 'https://www.imdb.com/search/title/?groups=top_1000&sort=year,desc'
def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")

soup = get_page_contents(url)

#extract movies
movies   = soup.findAll('h3', class_='lister-item-header')

'''
titles   = [movie.find('a').text for movie in movies]
release  = [movie.find('span', class_='lister-item-year text-muted unbold').text for movie in movies]

movie.find('div', 'inline-block ratings-imdb-rating')['data-value']

votes    = movie.findAll('span' , {'name' : 'nv'})[0]['data-value']
earnings = movie.findAll('span' , {'name' : 'nv'})[1]['data-value']

director = movie.find('p').find('a').text
actors   = [actor.text for actor in movie.find('p').findAll('a')[1:]]
'''

print (movies)

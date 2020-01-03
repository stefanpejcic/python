import bs4
import pandas as pd
import requests

url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")

soup = get_page_contents(url)

#extract movies
movies = soup.findAll('h3', class_='lister-item-header')
titles = [movie.find('a').text for movie in movies]
release = [movie.find('span', class_='lister-item-year text-muted unbold').text for movie in movies]



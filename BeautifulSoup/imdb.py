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
#set base url to imdb
with open('ajde.html', 'w') as f:
    f.write(str("<head>"))
    f.write(str('<base href="https://www.imdb.com" target="_blank">'))
    f.write(str('</head>'))
'''

with open('ajde.html', 'a') as f:
    for movie in movies:
        f.write(str(movie))

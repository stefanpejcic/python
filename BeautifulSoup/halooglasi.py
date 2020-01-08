import bs4
from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd?cena_d_from=18000&cena_d_to=30000&cena_d_unit=4&sort=defaultunit_cena_d%2Casc'
count = 0

def get_page_contents(url):
    page = requests.get(url, headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.88 Safari/537.36'})
    return bs4.BeautifulSoup(page.text, "html.parser")

soup = get_page_contents(url)

#extract oglasi
oglasi   = soup.findAll('div', class_='product-item')

with open('nekretnine.html', 'w', encoding="utf-8") as f:
    f.write(str("<head>"))
    f.write(str('<base href="https://www.halooglasi.com/" target="_blank">'))
    f.write(str('</head>'))
    for oglas in oglasi:
        f.write(str(oglas))

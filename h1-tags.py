import requests
from bs4 import BeautifulSoup

url = 'https://wporb.com/'
request = requests.get(url)
soup = BeautifulSoup(request.text, 'lxml')

for tag in soup.find_all('h1'):
    print("h1: "+tag.text.strip())

import requests
from bs4 import BeautifulSoup
url = 'https://wporb.com/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))

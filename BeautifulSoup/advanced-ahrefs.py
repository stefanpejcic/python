import requests
from bs4 import BeautifulSoup

url = 'https://wporb.com/'

response = requests.get(url)
text = response.text
soup = BeautifulSoup(text, 'lxml')

hrefs = []

a_tags = soup.find_all('a')

for tag in a_tags:
  href = tag['href']
  hrefs.append(href)
print("Found: ",len(hrefs), " links")
for h in hrefs:
  if h.count('/') > 1:
    print(h)

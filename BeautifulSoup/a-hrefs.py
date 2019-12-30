import requests
from bs4 import BeautifulSoup

'''
#from a local file
with open('file.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'lxml')
'''

#from a website
url = 'https://wporb.com/'
request = requests.get(url)
soup = BeautifulSoup(request.text, 'lxml')

for tag in soup.find_all('a'):
    print("Anchor text: "+tag.text.strip())

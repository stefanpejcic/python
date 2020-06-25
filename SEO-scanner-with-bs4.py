import requests
from bs4 import BeautifulSoup
url = 'https://' + input()
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')


class text_colors:
    MAGENTA = '\033[95m'
    BLUE= '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

title = soup.find("meta",  property="og:title")
description = soup.find("meta",  property="og:description")
url = soup.find("meta",  property="og:url")

print(100 * '_')
print(title["content"] if title else "No meta title given")
print(description["content"] if description else "No meta description given")
print(url["content"] if url else "No meta url given")
print(100 * '_')

counter = 0

for link in soup.find_all('a'):
    #print(link.get('href'))
    counter += 1

print (text_colors.MAGENTA + "Number of hrefs:"+ text_colors.ENDC)
print (counter)

counter = 0

for link in soup.find_all('h1'):
    #print(link.get('h1'))
    counter += 1

print (text_colors.BLUE + "Number of h1:"+ text_colors.ENDC)
print(counter)

counter = 0

for link in soup.find_all('h2'):
    #print(link.get('h2'))
    counter += 1

print (text_colors.GREEN + "Number of h2:"+ text_colors.ENDC)
print(counter)

counter = 0

for link in soup.find_all('img'):
    #print(link.get('h2'))
    counter += 1

print (text_colors.RED + "Number of images:"+ text_colors.ENDC)
print(counter)

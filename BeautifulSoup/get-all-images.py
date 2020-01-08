import urllib.request
from bs4 import BeautifulSoup

tf2_art = urllib.request.urlopen("http://www.teamfortress.com/artwork.php")
souped_tf2_art = BeautifulSoup(tf2_art, 'html.parser')
def remove_query(url):
    url = urllib.parse.urlparse(url)[1:3]
    url = url[0] + url[1]
    return url
    
print(souped_tf2_art.find_all('a'))

for img_url in souped_tf2_art.find_all('a'):
    #prints images
    print(img_url)
    try:
        img_url = img_url['href']
        if "http://media.steampowered.com/apps/tf2" in img_url:
            print("valid url: " + img_url['href'])
            img_name = remove_query(img_url).split("/")[-1]
            urllib.request.urlretrieve(img_url, img_name)
        else:
            print("invalid url: " + img_url['href'])
    except:
        print(img_url)

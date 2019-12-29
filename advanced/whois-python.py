from bs4 import BeautifulSoup
import requests
import re
import socket

url=input("Domain name: ")
site = 'http://www.iana.org/whois?q='+url
r = requests.get(site)
soup = BeautifulSoup(r.text, "html.parser")

for s in soup.findAll('pre'):
	regex = re.compile(r'<[^<]*?>')
	whois = regex.sub('', str(s))
	print (whois)

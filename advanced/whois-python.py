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

"""	
#If we wantto lookup a list
from bs4 import BeautifulSoup
import requests
import re
import socket

#have to 
url=["wporb.com", "giga.rs"]
for domain in url:
  site = 'http://www.iana.org/whois?q='+domain
  r = requests.get(site)
  soup = BeautifulSoup(r.text, "html.parser")

  for s in soup.findAll('pre'):
	  regex = re.compile(r'<[^<]*?>')
	  whois = regex.sub('', str(s))
	  print (whois)
"""

"""	
#and if we want to lookup a list of domains from lets say expireddomains.net
from bs4 import BeautifulSoup
import requests
import re
import socket

url=[]
# open file and read the content in a list
with open('domains.csv', 'r') as filehandle:
  for line in filehandle:
        # remove linebreak which is the last character of the string
        domain = line[:-1]

        # add item to the list
        url.append(domain)

for domain in url:
  site = 'http://www.iana.org/whois?q='+domain
  r = requests.get(site)
  soup = BeautifulSoup(r.text, "html.parser")

  for s in soup.findAll('pre'):
	  regex = re.compile(r'<[^<]*?>')
	  whois = regex.sub('', str(s))
	  print (whois)
"""

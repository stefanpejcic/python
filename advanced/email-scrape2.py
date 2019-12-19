import re, sys, urllib
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as url:
    response = url.read()

regex = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')

emails = regex.findall(response)
with open('emails.csv', 'w+') as email_file: 
    email_file.write('\n'.join(set(emails)))

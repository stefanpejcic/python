import re
import sys
import urllib

import urllib.request

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

with urllib.request.urlopen(sys.argv[1]) as url:
    response = url.read()

regex = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')

emails = regex.findall(response)
with open('emails.csv', 'w+') as email_file: 
    email_file.write('\n'.join(set(emails)))

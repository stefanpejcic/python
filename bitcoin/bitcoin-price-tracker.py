import requests
import time

# user inputs
alert_amount = input('Alert if Bitcoin drops below: ')

while True:
  url = "https://api.coindesk.com/v1/bpi/currentprice.json"
  response = requests.get(
    url, 
    headers={"Accept": "application/json"},
  )
  data = response.json()
  bpi = data['bpi']
  USD = bpi['USD']
  bitcoin_rate = int(USD['rate_float'])

  if bitcoin_rate < int(alert_amount):
    print('Price is ' + str(bitcoin_rate) + '. Will check again in 1 minute. Ctrl + C to quit.')
    time.sleep(60)
  else:
    time.sleep(300)
    print('Price is ' + str(bitcoin_rate) + '. Will check again in 5 minutes. Ctrl + C to quit.')


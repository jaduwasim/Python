'''
Communication with coindest application to get

if we send http requests to coindest application 
it will provide current price information

we send http rquest from python application by using request module.
we have install this modules sepatetly

pip install requests

we can send request to coindesk application by using urls :https://api.coindesk.com/v1/bpi/currentprice.json
'''


import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
binfo = response.json()
print(type(binfo))
print('-'*50)
print(binfo)
print('-'*50)
print(binfo['time']['updateduk'])
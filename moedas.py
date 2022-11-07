import requests
import json
import time

c = 0
while c == 0:
    time.sleep(5)
    bitcoin = requests.get('https://economia.awesomeapi.com.br/json/last/BTC-BRL').json()
    etherium = requests.get('https://economia.awesomeapi.com.br/json/last/ETH-BRL')
    etherium2 = etherium.json()
    #print(etherium2)
    #print(bitcoin)
    print('Etherium', etherium2['ETHBRL']['bid'], '|||||  Bitcoin: ', bitcoin['BTCBRL']['bid'])

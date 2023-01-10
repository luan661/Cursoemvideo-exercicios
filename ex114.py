import requests

try:
    r = requests.get('http://pudim.com.br')
except:
    print('\033[31mSite www.Pudim.com.br indisponível no momento.\033[m')
else:
    print('\033[32mSite www.Pudim.com.br online.\033[m')

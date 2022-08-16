import requests
from bs4 import BeautifulSoup
import json
import os
import time

# the target we want to open    
#url='https://www.angeloni.com.br/super/p/batata-doce-kg-164828'
#url='https://www.angeloni.com.br/super/p/leite-tirol-integral-1l-3852102'
#url='https://www.angeloni.com.br/super/p/alho-granel-kg-1475278'
#url='https://www.angeloni.com.br/super/p/tomate-italiano-kg-786934'

#open with GET method
#print(url)
#resp=requests.get(url)
#print(resp)
#http_respone 200 means OK status
#soup = BeautifulSoup(requests.get(url).content, "html.parser")
#print(soup)
#data = [json.loads(x.string) for x in soup.find_all("script", type="application/ld+json")]
#print(data)

#print(data[1].keys())
#print(data[1].items())
#print(data[1].get('name') + " - R$" + data[1].get('offers').get('price'))
print("---------------------------------------------")
for url in open('Angeloni.txt'):
    #open with GET method
    print(url)
    resp=requests.get(url)
    time.sleep(1)
    print(resp)
    #http_respone 200 means OK status
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    time.sleep(1)
    print(soup)
    data = [json.loads(x.string) for x in soup.find_all("script", type="application/ld+json")]
    time.sleep(1)

    print(data)
    #print(data[1].keys())
    #print(data[1].items())
    #print(data[1].get('name') + " - R$" + data[1].get('offers').get('price'))
import requests
from bs4 import BeautifulSoup

source = requests.get('https://premiumproxy.net/full-proxy-list').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

ttr = soup.find_all('tr', class_='pp1x')
#print(ttr)

for i in ttr:
    #print(i)
    #print()
    #print('IP Proxy: Port', i.td.font.text)

    
    for k in i.find_all('td'):
        print(k)
        #print(k.text)
        print()
        #print('IP Proxy: Port '+ k.text)
            
       


from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.pricebefore.com/mobiles/').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

tag = soup.find_all('div', class_='col-right')
#print(tag)

for i in tag:
    #print(i)
    z = i.find('div', class_='title').b.a.text
    print("Mobile name: ", end=" ")
    print(z)

    for j in i.find_all('div', class_='item'):
        y = j.text
        print(y)
    print()
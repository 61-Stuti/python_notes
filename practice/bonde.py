import requests
from bs4 import BeautifulSoup

source = requests.get('https://bondeabhijeet.github.io/Anime-torrent-listing.html').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

tagdiv = soup.find_all('div', class_='col-xl-6 col-lg-6 col-md-12 col-sm-12')
#print(tagdiv)

for i in tagdiv:
    print('Box: ', i.find('div', class_='about_box').h3.text)

    for k in i.find_all('a'):
        print('Link: ', k['href'])
    print()
        
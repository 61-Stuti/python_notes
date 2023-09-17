from bs4 import BeautifulSoup
import requests

for page in range(1,11):
    source = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html').text
    soup = BeautifulSoup(source, 'lxml')
    #print(soup.prettify())

    print('Books on page ', page)
    print()
    print()

    tag = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    #print(tag)

    for i in tag:
        z= i.find('h3').a['title']
        print('name of the book: ', z)
        print()
    print()

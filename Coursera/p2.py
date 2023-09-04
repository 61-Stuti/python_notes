from bs4 import BeautifulSoup
import requests

with open("practice2.html") as html_file:
    soup =  BeautifulSoup(html_file, 'lxml')

print(soup.prettify())

for article in soup.find_all('div', class_= 'atricle'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

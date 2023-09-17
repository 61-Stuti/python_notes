from bs4 import BeautifulSoup
import requests

f = open('practice4.txt', 'w+', encoding='UTF-8')
print(f.readline())

source = requests.get("https://docs.python.org/3/howto/index.html").text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

data = soup.find_all(class_='reference internal')

for i in data:
    print(i.text)
    print('Link: ', i['href'])
    print()

    f.write('Heading: ' + i.text + '\n')
    f.write('Link: ' + i['href'] + '\n')
    f.write('\n')

f.close()

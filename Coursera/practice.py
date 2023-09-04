import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

count = 10

f = open('practice2.txt', 'w+', encoding='UTF-8')

for i in range(1,count+1):
    fle = urllib.request.urlopen(f"https://quotes.toscrape.com/page/{i}/").read()
    soup = BeautifulSoup(fle, 'html.parser')
    #print(soup.prettify())

    a = soup.find_all(class_='quote')
    #print(a)
    
    for i in a:

        f.write('Quote:' + i.find(class_='text').text + '\n')
        f.write('Author:' + i.find(class_='author').text + '\n')
                
        print('Quote: ', i.find(class_='text').text)
        print('Author: ', i.find(class_='author').text)
        print('Tags: ', end = ' ')    

        str1 = ''

        try:
            for k in i.find_all('a', class_='tag'):

                str1 += k.text + ', '
            

                print(k.text, end = ' ')
            print()

        except:
            continue
        
        f.write('Tags:' + str1 + '\n')

f.close()
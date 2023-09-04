import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

count = 10

f = open('textfile.txt', 'w+', encoding ='UTF-8')


for i in range(1,count+1):
    fle = urllib.request.urlopen(f"http://quotes.toscrape.com/page/{i}/").read()
    soup = BeautifulSoup(fle, 'html.parser')
    print(soup.prettify())

    z = soup.find_all(class_='quote')                #all tags with class quote
    #print(z)

    for i in z:
        f.write('Quote:'+ i.find(class_='text').text +'\n')
        f.write('Author:' + i.find(class_='author').text +'\n')
        
        print('Quote:', i.find(class_='text').text)          #find gives single tag with that particular class
        print('Author:', i.find(class_='author').text)
        print('Tags:', end=' ')
        
        str1 = ""
        try:
            for k in i.find_all('a', class_='tag'):          #finds all the anchor tags where class = tag
                str1 += (k.text + ', ')
                
                print(k.text, end=' ')                     #prints value one by one from the list of tags
            print()

        except:
            continue
        f.write('Tags:' + str1 + '\n' + '\n')

f.close()


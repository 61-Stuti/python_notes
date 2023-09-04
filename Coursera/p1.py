import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

fle = urllib.request.urlopen("https://www.timeanddate.com/worldclock/").read()
soup = BeautifulSoup(fle, 'html.parser')
#print(soup.prettify())

tags = soup('td')
#print(tags)

for i in tags:

    if len(i('a'))!=0:                   #list
        print(i('a')[0].text)            #empty list cant be none
        
    
   # if i.find('a')!= None:             #string, none is not equal to zero
    #    print(i.find('a').text)

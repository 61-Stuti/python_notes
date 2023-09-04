import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

position = 18
count = 7
url = "http://py4e-data.dr-chuck.net/known_by_Clarke.html"

for i in range(0,count):


    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())

    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[position-1]['href']

print(tags[17].text)

#OR

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

count = 7
position = 18

url = "http://py4e-data.dr-chuck.net/known_by_Clarke.html"

for i in range(0, count+1):
    
    fle = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(fle, 'html.parser')
    
    tags = soup('a')
    url = tags[position-1]['href']
    

print(soup('h1')[0].text.split()[2])    





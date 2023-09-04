import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1851329.html').read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

tags = soup('span')
#print(len(tags))
print(tags)

Sum = 0
for i in tags:
    z = int(i.text)
    Sum = Sum + z
print(Sum)

#OR

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

sum = 0
fle = urllib.request.urlopen("https://py4e-data.dr-chuck.net/comments_1851329.html").read()
soup = BeautifulSoup(fle, 'html.parser')
#print(soup.prettify())

z = soup.find_all(class_='comments')
#print(z)

for i in z:
    print(i.text)
    sum += int(i.text)

print(sum)
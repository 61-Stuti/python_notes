import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1851329.html').read()
soup = BeautifulSoup(html, 'html.parser')


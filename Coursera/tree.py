import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

fle = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1851331.xml").read()
lst2 = list()

tree = ET.fromstring(fle)
lst = tree.findall("comments/comment")

for i in lst:
    lst2.append(int(i.find('count').text))
print(sum(lst2))


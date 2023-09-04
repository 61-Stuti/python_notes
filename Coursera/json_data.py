import urllib.request, urllib.parse, urllib.error
import json

fle = urllib.request.urlopen(" http://py4e-data.dr-chuck.net/comments_1851332.json").read()

lst= list()
info = json.loads(fle)

for i in info['comments']:
    lst.append(int(i['count']))

print(sum(lst))
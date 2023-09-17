import requests

payload = {'page': 2, 'count': 25}
r = requests.get('http://httpbin.org/get', params = payload)
# get parameter is included in the url
# payload is the dictionary of paramaters

print(r.text)
print(r.url)
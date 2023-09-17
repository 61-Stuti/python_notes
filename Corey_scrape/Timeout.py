import requests

#r = requests.get('http://httpbin.org/delay/1', timeout=3)

r = requests.get('http://httpbin.org/delay/6', timeout=3)
#'http://httpbin.org/basic-auth/stuti/nigam', timeout=3
#6 seconds to respond and timeout is 3 secs
#exception is ReadTimeout

print(r)
#3 seconds of timer
import requests

payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('http://httpbin.org/post', data = payload)
#data thta has been posted

print(r.text)
print()
print(r.json())
#from json it created a dictionary
print()

r_dict = r.json()
print(r_dict['form'])
#to access the form key
print()
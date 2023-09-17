import requests
r= requests.get('http://httpbin.org/basic-auth/stuti/nigam', auth=('stuti', 'nigam'))

#pass in the parameters in the form of tuples where username and pswd should be there

print(r.text)
print(r)  #Response [200]

#we are authenticated
# if i pass wrong credentials then no response text

#so i print(r) then response 401 will be the output which shows the error


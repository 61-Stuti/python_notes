import requests

source = requests.get(' https://imgs.xkcd.com/comics/python.png')
#content prints out bytes of the image
print(source.content)

with open('comic.png', 'wb') as f:
    f.write(source.content)

print(source.status_code)   #200 success, 300- redirects, 400- errors, 500- major error
#or
print(source.ok)
print(source.headers)
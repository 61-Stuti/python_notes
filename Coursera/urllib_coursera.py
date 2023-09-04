import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen("http://data.pr4e.org/intro-short.txt")
for line in file:
    print(line.decode().strip())

#like a file
import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen("http://data.pr4e.org/intro-short.txt")

count = dict()
for line in file:
    words= line.decode().split()

    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)
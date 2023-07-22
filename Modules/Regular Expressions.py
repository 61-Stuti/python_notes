#Regular expressions library - re

#phone number: (555)-555-5555
#regex pattern: r"(\d\d\d)-\d\d\d-\d\d\d\d"     - \d:identifiers, indicates digits
#r"(\d{3})-\d{3}-\d{4}"

import re

sentence = "the agent's phone number is 555-888-1234. Call soon on his phone number!"

pattern = "phone number"
match = re.search(pattern,sentence)
#search  finds the match in the string
print(match)
#finds the span of the match in the string
print(match.span())
print(match.start())
print(match.end())

#findall search all the matches in the string
matches = re.findall(pattern,sentence)
print(matches)

print(len(matches))

#finditer is mix of search and findall, it finds all the repeats in the string and its span and match
for match in re.finditer(pattern, sentence):
    print(match)
    print(match.group())


number = re.search(r'\d{3}-\d{3}-\d{4}', sentence)
print(number)

number_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
results = re.search(number_pattern, sentence)
print(results.group()) 
print(sentence)
#print(results.group(1)) -> 555


#pipe operator | -> represents OR

print(re.search(r'cat|dog', "there's a dog."))

# . represents wild operator meaning after . whether it matches the syntax or not

print(re.findall(r'.at', "there is cat and bat on sat"))

# ^\d when a string starts with an actual digit

print(re.findall(r'^\d', "2 boys are present"))

#\d$ represents string ends with a digit

print(re.findall(r'\d$', "my dob is 6"))

# [^]+ for excluding

clean = re.findall(r'[^.?!]+', "wow! you are cute. how so cute?")
print(' '.join(clean))

#to find alphanumerics
text = 'This sentence has hypen-word which are long-ish.'
pattern = r'[\w]+'
print(re.findall(pattern, text))

pattern = r'[\w]+-[\w]+'
print(re.findall(pattern, text))

text1 = 'im a catfish'
text2 = 'im a catnap'
text3 = 'im a caterpillar'

pattern = r'cat(fish|nap|erpillar)'
print(re.search(pattern,text2))

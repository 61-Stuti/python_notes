print("hello")

name="stuti"
print(name)

name="bonde"
print(f"my name is {name}")

name1="stuti"
name2="nigam"
print(f"my name is {name1} {name2}")     #f string

print(name1,end=" ")
print(name2, end=" ")
print("biotech")

name3 = "Stuti"
print(name3)
print(name3[2:5])
print(name3[2:])
print(name3[:4])
print(name3[1:4])
print(name3 * 3)
print(name3 + " " + "Nigam")
print(name3 + " Nigam")
print((name3 + " " + "Nigam" + " ") * 3)
print(name3[1:5] + " " + name2[2:5])
print(name3[:2] + name3[3:5])
print(name3[0:5:2])                                #[start:stop:step]
print(name3[::2])                                  
print(name3[-1])           
print(name3[-1:-6:-2])
print(name3[5:-6:-2])
print(name3[5::-2])
print((name3 + " ") * 3 + " " + ("Nigam" + " ") * 4 )

#substrings
sentence="My name. is stuti."
print(sentence.split())

sentence2="coco is my. dog's name."
print(sentence2.replace(".",""))

sentence2="coco is my. dog's name."
print(sentence2.replace(".","").split())

sentence3="  i am stuti  "
print(sentence3.strip())
print(sentence3.rstrip())
print(sentence3.lstrip())


num = 9969
nums = str(num).replace('',' ').split()

for i in range(0,len(nums)):
    if nums[i] == '6':
        nums[i] = '9'
        break
print(int("".join(nums)))
print("s".join(nums))


needle = 'sad'
haystack = 'sadaboutsad'

import re
match = re.search(needle,haystack)
print(match.span())
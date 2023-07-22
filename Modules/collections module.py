# Counter class

#counter is technicallyy dictionary subclass where object are stored as dictionary keys 
#and counts as values so its is specialized dictionary

from collections import Counter
mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,3]     #gives the output in the form of the list
print(Counter(mylist))

mystring = ['a','a',10,10]
print(Counter(mystring))     

name = "stuti"
print(Counter(name))

sentence =  "my name is Stuti and my friend's name is bonde"
print(Counter(sentence.lower().split()))

wow = "aaaaaabbbbbccccddddddddddddd"
c = Counter(wow)
print(c.most_common(2))
print(c.most_common())
print(list(c))                                  #prints the keys and not the count


#default dictionary
#if a key is not present in dictionary and you encounter them so normal dictionary will give an error

d = {'a' : 10}
print(d['a'])

#print(d['wrong])

from collections import defaultdict
#In default dictionary using the lambda function it will assign 0 value to the key which is not present in the dictionary

d = defaultdict(lambda : 0)                # assign 0 values to all the keys
d['correct'] = 100
print(d['wrong'])
print(d)


# namedtuple

mytuple = (10,20,30)
print(mytuple[0])

from collections import namedtuple

#more like a class (typename, attributes) where dog is an object
#mix of class and tuple
Dog = namedtuple('Dog', ['age', 'breed', 'name1'])
Sammy = Dog(age = 10, breed = 'Husky', name1= 'Sam')
print(Sammy)
print(Sammy.age)
print(Sammy[0])
print(Sammy.breed)
print(Sammy[2])
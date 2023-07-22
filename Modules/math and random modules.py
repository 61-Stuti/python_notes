#math
import math
value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(value))
print(math.pi)
print(math.e)


#Numpy
#library for numerical purpose and has more functions than python's built in libraries
print(math.log(math.e))
print(math.tan(45))
print(math.degrees(math.pi/2))
print(math.radians(180))


#random
import random
random.seed(101)
print(random.randint(0,100))

#SAMPLE WITH REPLACEMENT
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))
print(random.choices(population=mylist, k=10))   #where k = how many numbers i want from the list

#SAMPLE WITHOUT REPPLACEMENT
print(random.sample(population=mylist, k=10))

random.shuffle(mylist)
print(mylist)

print(random.uniform(a=10, b=20))                 #prints float values
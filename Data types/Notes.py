name="hello world"                 #String are immutable
#name[0]="P"
new_name= name[1:]
print("P"+ new_name)               #string interpolation

new_name= "P"+ new_name
print(new_name)

print(new_name.split('l'))

print("The {} {} {}".format("fox", "brown", "quick") )
print("The {2} {1} {0}".format("fox", "brown", "quick") )
print("The {0} {0} {0}".format("fox", "brown", "quick") )
print("The {q} {b} {f}".format(f="fox",b= "brown",q= "quick") )
 
result= 100/777                                                     #float format
print("the result was {}".format(result))
print("the result was {r:1.3f}".format(r=result))                   #value:width.precision f

#Sets -> unordered collection of unique objects
myset= {1,2,3}
print(myset)
myset.add(4)
print(myset)

li=[1,1,1,1,2,2,3,4,4,4,4,3,3,3]
print(set(li))

#Booleans
print(1>2)

#pass - does nothing at all

x=[1,2,3]

for i in x:
    pass
print("end of this")

#continue - goes to the top of closest enlcosing loop

x="stuti"

for i in x:
    if i=='u':
        continue
    print(i)

#break - break out of the current closest enclosing loop

x="stuti"

for i in x:
    if i=='u':
        break
    print(i)

x=0
while x<5:
    if x==2:
        break
    print(x)
    x+=1

#enumerate

word="abcde"

for i in enumerate(word):      #presents the index andword in the form of tuple
    print(i)

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")

#zip                                    #for the list with same length
list1 =[1,2,3]
list2=['a','b','c']
list3=[100,200,300]

for i in zip(list1, list2, list3):
    print(i)
    
print(list(zip(list1, list2, list3)))


#input funations always accept input as a string

result = int(input("favourite number: "))
print(result)
print(type(result))

if result.isdigit():
    print("True")
else:
    pass





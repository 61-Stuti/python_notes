L=["stuti", "bonde", "abhijeet"]
print(L)

for i in L:
    print(i)

for i in range (0, len(L)):
    print(i)

for i in range (0, len(L)):
    print(L[i])

L[0]= "names"
print(L)

print(L.pop())                    
print(L)

L.append("abhijeet")
print(L)
print( L.pop(1))

new_list= ['a','b','x','o','n']
new_list.sort()
print(new_list)

sorted(new_list)
print(new_list)

new_list.reverse()
print(new_list)

my_list=[1,2,[3,4]]
print(my_list[2][1])

my_list.insert

L1=["stuti", "nigam", "coco"]
L2=["abhijeet","bonde", "billi"]
for i in L1:
    for j in L2:
        print(i,j)

mystring= "stuti"
List1=[letter for letter in mystring]
print(List1)

celsius= [0,10,20,30,40]
fahrenheit= [((9/5)*Temp + 32) for Temp in celsius]
print(fahrenheit)

mylist= [x*y for x in [1,2,3] for y in [1,10,100]]
print(mylist)
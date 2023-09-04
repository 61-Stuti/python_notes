def search(lst, x):

    for i in range(0,len(lst)):
        if lst[i]==x:
            return i
    return -1

lst = [1,20,30,45]
x=20

print(x, 'is present at', search(lst,x))



#If (n) is even then our output will be 0
#If (n) is odd then our output will be the sum of the elements of the array.

def add(lst):
    n = len(lst)
    if n%2 == 0:
        return 0
    else:
        return sum(lst2)
    
lst2 = [1,2,3,4,5,6,7]
print(add(lst2))

#OR

def add(lst,n):
    if n%2 ==0:
        return 0
   
    Sum = 0
    for i in range(n):
        Sum += lst[i]
    return Sum
    
lst2 = [1,2,3,4,5,6]
n1 = len(lst2)

lst3 = [1,2,3,4,5,6,7]
n2=len(lst3)

print(add(lst2, n1))
print(add(lst3, n2))


#Best case: order of growth constant becoz n is even
#avg case: n is likely to bhi even or odd, order of growth linear
#worst case: order of growth linear becoz n is always odd
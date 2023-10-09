def search(lst, target):
    left = 0
    right = len(lst)-1

    while left<= right:
        mid = (left+right)//2

        if lst[mid]== target:
            return mid
        elif lst[mid]< target:
            left = mid+1
        else:
            right = mid-1

    return -1

lst= [1,2,3,4,15,18,20,21]
target = 18
result= search(lst, target)
print(result)
print(len(lst))




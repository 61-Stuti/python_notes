def selectionsort(lst, n):

    for i in range(n):
        min= i 

        for j in range(i+1,n):
            if lst[j]<lst[min]:
                min = j

        (lst[i],lst[min])= (lst[min],lst[i])


lst = [-2, 45, 0, 11, -9,88,-97,-202,747]
n = len(lst)

selectionsort(lst,n)
print("sorted array: ")
print(lst)


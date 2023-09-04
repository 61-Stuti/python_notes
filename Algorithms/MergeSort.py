def MergeSort(lst):
    L= list()
    R= list()

    if len(lst)>1:

        mid = len(lst)//2

        L = lst[:mid]

        R = lst[mid:]

        MergeSort(L)

        MergeSort(R) 

    i = j = k = 0

    while i<len(L) and j< len(R):
        if L[i]<=R[j]:
            lst[k] = L[i]
            i+= 1
        
        else:
            lst[k]= R[j]
            j+= 1

        k+= 1

    while i< len(L):
        lst[k]= L[i]
        i+=1
        k+=1

    while j< len(R):
        lst[k]= R[j]
        j+=1
        k+=1

def printlst(lst):
    for i in range(len(lst)):
        print(lst[i], end=" ")
    print()
    
lst = [31,24,15,46,7] 

print("Normal List: ")
printlst(lst)

MergeSort(lst)
print("Sorted list: ")
printlst(lst)



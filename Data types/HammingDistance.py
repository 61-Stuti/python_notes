x=1
y=4
check=0
a= f"{x:032b}"
b= f"{y:032b}" 
for i in range(0,len(a)):
    if (a[i]!=b[i]):
        check= check+1

print(check)


#(coordinates[1][1] - coordinates[0][1]) * (coordinates[2][0] - coordinates[0][0]) == (coordinates[2][1] - coordinates[0][1]) *(coordinates[1][0] - coordinates[0][0])


L = [1,2,3]
print(len(L))
x=1
y=4
check=0

a= f"{x:032b}"
b= f"{y:032b}" 
for i in range(0,len(a)):
    if (a[i]!=b[i]):
        check= check+1

print(check)





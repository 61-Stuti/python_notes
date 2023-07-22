a=4
if (a<10):
    if (a<5):
        print("a<5")
    else:
        print("a is not smaller than 5")
    print(a)
else:
    print("error")



if (a==7):
    print(a)
else:
    print("a!=7")



if (a==7):
    print("a=7")
elif (a==8):
    print("a=8")
elif (a==9):
    print("a=9")
else:
    print(a)


print(True) if a<5 else print(False)

#one line ifelse

results=[x if x%2==0 else 'odd' for x in range(10)]
print(tuple(results))
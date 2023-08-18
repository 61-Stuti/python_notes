def add(n1, n2):
    sum = n1 + n2
    return sum
y = add(10,20)
print(y)

number1 = 20
number2 = input('Enter a number: ')

z = add(number1, number2)
print(z)
print("error")
#since there's is an error in the code so after print(z), nothing will be printed


try:
    result = 10 + '10'
    print(result)
except:
    print("Hey it's looks like something bad happened")

#in this try statment is wrong, still except statement is getting executed
#even if there is an error we continue with some more code
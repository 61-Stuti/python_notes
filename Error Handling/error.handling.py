def add(n1,n2):
    sum = n1 + n2
    return sum
z = add(10,20)
print(z)

number1 = 20
number2 = 20
z = add(number1, number2)
print(z)
print("error in printing")
#if there is an error then the line which is having an error, code after that line will not be executed


try:
    # WANT TO ATTEMPT THIS CODE
    #MAY HAVE AN ERROR

    result = 10 + '10'

except:                                                 #except statement is executed if there is any kind of error
    print("hey it looks you aren't adding correctly")
else:
    print("add went well")
    print(result)


try:
    f = open("Functions", 'w')
    f.write("write a test line")
except TypeError:
    print("There's a typeerror")
except OSError:
    print("There's an OSError")
finally:
    print('i always run')


try:                                    #block of code you're trying to attempt
    f = open("Functions", 'r')
    f.write("write a test line")
except :                               #it occurs when there's and error in your try statement
    print("All other errors")
finally:                                # always run whethere there's and error or not
    print('i always run')
#error youre writing something in read only mode


def add_an_int():

    while True:
        try:
            number = int(input("Please provide a number: "))
        except:
            print("Whoops1 it's not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("end of try, except and finally")
            print("I'll always run")
z = add_an_int()
print(z)

def ask():
    while True:
        try:
            number = int(input("Please provide an integer: "))
            result = number ** 2
        except:
            print("An error occured, please try again")
            continue
        else:
            print(f"Here's your {result}")
            break
        finally:
            print("All Done")
z = ask()
print(z)
#local
lambda num: num**2

name= "THIS STATEMENT IS GLOBAL"
def greet():                                             #enclosing local function

    name= 'Sammy'
    def hello():
        print("hello " +name)

    hello()

greet()                                                #enclosing local function



#global
name= "THIS STATEMENT IS GLOBAL"
def greet():                                             
    #enclosing
    #name= 'Sammy'
    def hello():
        #local
        print("hello " +name)               #in hello function name is not locally present then in enclosing also name variable is not
                                            #present so it searches name function globally and then print it
    hello()

greet()   


#and above global comes the built in function


x = 50

def func(x):

    print(f'X is {x}')

    #LOCAL REASSIGNMENT

    x = 'NEW VALUE'
    print(f'I just locally assigned to {x}')
    return x

print(x)
x = func(x)
print(x)


x=50

def func(x):

    print(f'value of {x}')

# locally assigning value to x
    x='new value'

    print(f'I just locally changes global x to {x}')
    return x
print(x)
x= func(x)
print(x)
       
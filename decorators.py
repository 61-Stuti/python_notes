def hello():
    return "hello"
z = hello()
print(z)

def hello():
    return "hello"
greet = hello                #functions are objects that can be pass into other objects
z = greet()
print(z)
del hello                    #hello is deleted so it cant be printed but greet can still be printed  
print(z)

def hello(name = 'Jose'):
    print("i am hello function")

    def greet():
        print("\t I'm greet func")

    def welcome():
        print("\t Welcome ot welcome function")

    print("I'm going to return a function")
    if name == 'Jose':
        print(greet())
    else:
        print(welcome())
    
z = hello
print(z())

def cool():
    def super_cool():
        return "I'm supercool"
    return super_cool
z = cool()
print(z())


def hello():
    return "I'm Jose"

def other(super_func):
    print("This is a statement")
    print(super_func())

print(other(hello))
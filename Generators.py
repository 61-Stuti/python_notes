def create_cubes(n):
    result = []
    for i in range(n):
        result.append(i**3)
    return result
z = create_cubes(10)
print(z)
for i in create_cubes(10):
    print(i)


#Use of Yield statement to save the memory of the code

#https://java2blog.com/print-generator-object-python/

def create_cubes(n):
    for i in range(n):
        yield i**3
for z in create_cubes(10):
    print(z)

def generate_fibon(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b
print(*generate_fibon(10))
for number in generate_fibon(10):
    print(number)


def fib2(n):                   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
z = fib2(10)
print(z)


#Iteration 
def simple_gen(n):
    for i in range(n):
        yield i
z = list(simple_gen(3))
print(z)

#In generator you can directly do the iteration using the *next* function

# next function is used
g =  simple_gen(3)           #list, string object is not an iterator. for eg g=z
print(next(g))                    #using for loops in list and string you can do iteration
print(next(g))
print(next(g))

#iter function is used to generate the string
s = "hello"
s1 = iter(s)
print(next(s1))
print(next(s1))
print(next(s1))
print(next(s1))
print(next(s1))
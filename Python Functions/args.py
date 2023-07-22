def myfunc(*args):                                  #arguments
    return sum(args) * 0.05
d= myfunc(10,20,30,40)
print(d)

def myfunc(*args):
   print(args)
myfunc(10,20,30,40)    #args treats everything as a tuple inside function, returns back a tuple

def myfunc(*args):
   for items in args:
      print(items)
myfunc(10,20,30,40)

def myfunc(**kwargs):     #returns back a dictionary, keyword arguments
    print(kwargs)
    if "fruit" in kwargs:
      print("My favourite fruit of choice is {}".format(kwargs["fruit"]))
    else:
      print(" I didnot have a fruit of choice")
myfunc(fruit="apple", veggie="tomato")


def myfunc(*args, **kwargs):
   print(args)
   print(kwargs)
   print("I would like {} {}".format(args[0], kwargs['food']))

myfunc(10,20,30,fruit='apple',food= 'eggs', animal= 'dog')
      
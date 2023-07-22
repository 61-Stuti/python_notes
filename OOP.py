#camel casing for the class not snake casing like in function
#create instance of a dog class

class Dog():                   # Dog is the name of the class

    #CLASS OBJECT ATTRIBUTE
    species = 'mammal'  # this attribute is not connected to self, is not connected to any instance

    #attributes
    #we take it in argument
    #assign it using it self.attribute_name
    #attributes are not functions, they are just characterstics of the object

    def __init__(self, breed, name, spots):                # init method , reserved
        # parameter name = attribute name                  # self is a keyword with the reference to the class
        #self.breed = mybreed                              # instance of the class has .attributes
        self.breed = breed
        self.name = name
        self.spots = spots

# Operations/ actions/ methods
# method is a function inside a class

    def bark(self,age):
        print("Woof! My name is {} and I'm {} years old".format(self.name,age)) #since age is not an instance of the class

my_dog = Dog(breed= 'Pomeranion', name = 'Coco', spots = False)
z = type(my_dog)
print(z)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
print(my_dog.bark(2))


class Circle():
    pi = 3.14

    def __init__(self, radius = 1):             #default value of radius
        self.radius = radius
        self.area = radius * radius * Circle.pi
    def get_circumference(self):
        return 2 * Circle.pi * self.radius
    
e = my_circle = Circle(30)
print(e)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)

        
     
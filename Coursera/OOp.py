class PartyAnimal:
    x=0

    def party(self):
        self.x=self.x + 1
        print(self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()

####################################################################################################

class PartyAnimal:
    x=0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x=self.x + 1
        print(self.x)

    def __del__(self):
        print('I am constructed', self.x)    #this prints the last value of an before getting destructed, once the program ends.. 
                                             #it calls all the destructors               

an = PartyAnimal()
an.party()
an.party()
an.party()

an=42        #destructor
print(an)

################################################################################################################

class PartyAnimal:
    x = 0
    name = ''

    def __init__(self,nam):  #self is the instance itself which points to under construction and z is the parameter
        self.name = nam
        print(self.name,'constructed')

    def party(self):
        self.x = self.x+1
        print(self.name,'party count', self.x)

class FootballFan(PartyAnimal):   #extension class of partyanimal or subclass
    points= 0 
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, ' points', self.points)


s= PartyAnimal('Sally')
s.party()

j= FootballFan('Jim')
j.party()                 #at the moment of constrctor x is 0 then it is 1 when code is executed
j.touchdown()

##########################################################################################################################################
# 2 independent instances

class PartyAnimal:
    x = 0
    name = ''

    def __init__(self,z):  #self is the instance itself which points to under construction and z is the parameter
        self.name = z
        print(self.name,'constructed')

    def party(self):
        self.x = self.x+1
        print(self.name,'party count', self.x)

s = PartyAnimal('Sally')
s.party()

j=PartyAnimal('Jim')
j.party()
s.party()
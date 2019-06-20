'''
Private attributes should only be used by the owner. i.e. inside of the class definition itself.

Protected(restricted) attributes may be used, but at your own risk. Essentially, this means that
they should only be used under certain conditions.

Public attributes can and should be freely used.
'''

'''
Naming  Type        Meaning
name    Public      These attributes can be freely used inside or outside of a class definition.

_name   Protected   Protected attributes should not be used outside of the class definition, unless
                    inside of a subclass definition.

__name  Private     This kind of attribute is inaccesible and invisible. Its neither possible to read
                    nor write to those attributes, except inside of the class definition itself.

'''

class A():

    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

x = A()
x.pub

x.pub = x.pub + " and my value can be changed"
x.pub

x._prot

x.__priv

'''Even though __priv is an attribute the Attribute error says that the class has no attribute __priv
This is perfect information hidining'''


'''Data Encapsulation means, that we should only be able to access private
attributes via getters and setters.'''


class Robot:
    '''usage of private, protected and public attributes of the Robot class'''

    def __init__(self,name = None, build_year = 2000):
        '''initializer of Robot class'''
        self.__name = name
        self.__build_year = build_year
    
    def say_hi(self):
        '''prints hello message'''
        if self.__name:
            print("Hi, I am "+ self.__name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self,name):
        '''setter for name'''
        self.__name = name

    def get_name(self):
        '''getter for name'''
        return self.__name
    
    def set_build_year(self, by):
        '''setter for build_year'''
        self.__build_year = by
    
    def get_build_year(self):
        '''getter for build year'''
        return self.__build_year
    
    def __repr__(self):
        return "Robot('"+ self.__name + "', " + str(self.__build_year) + ")"
    
    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " + str(self.__build_year)

if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)

    for rob in [x, y]:
        rob.say_hi()

        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)

        print("I was built in the year " + str(rob.get_build_year()) + "!")


# Destructor

class Robot():
    '''robot class definition'''

    def __init__(self, name):
        '''initializer'''
        print(name + " has been created")

    def __del__(self):
        print("Robot has been destroyed")

if __name__ == "__main__":
    x = Robot('Tik-Tok')
    y = Robot('Jenkins')

    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y

"""personalizing the del method raises error"""

class Robot():
    '''robot class definition'''

    def __init__(self, name):
        '''initializer'''
        self.name = name
        print(name + " has been created")

    def __del__(self):
        print(self.name + ' says bye-bye!')

if __name__ == "__main__":
    x = Robot('Tik-Tok')
    y = Robot('Jenkins')

    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y



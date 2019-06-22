'''
getters and setters are used to ensure data encapsulation.
they are also called as mutator methods.

Data Encapsulation: Bundling of data with the methods that operate on these data.

According to Data Encapsulation principle the attributes needs to be private and all the 
necessary modifications should be done by the mutator methods.

NOTE: The Pythonic way to introduce attributes is to make them public.
'''

class P:
    'class definition for the class P'

    def __init__(self, x):
        'initializer method'
        self.__x = x
    
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x

p1 = P(42)
p2 = P(123)

p1.get_x()
p1.set_x(23434)

p1.set_x(p1.get_x() + p2.get_x())
p1.get_x()

'''
p1.set_x(p1.get_x() + p2.get_x()) is nothing but p1.x = p1.x + p2.x
but the former javaesque way is ugly.
'''
# To make it more pythonic we will use pulic instance attribute.

class P:

    def __init__(self, x):
        self.x = x

p1 = P(234)
p2 = P(64)

p1.x

p1.x = p1.x + p2.x
p1.x

class P:
    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        
        elif x > 1000:
            self.__x = 1000
        
        else:
            self.__x = x
    
p1 = P(1001)
p1.get_x()

p2 = P(10)
p2.get_x()

p2 = P(-10)
p2.get_x()

# NOTE: Python offers the best of both the worlds, we can have getters and setters so that we can 
# have a uniform interface to the outside world and change the implementation anytime we need
# BUT
# also provides us 'Properties'

# Demo of Properties

class P:

    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    


p1 = P(1001)
p1.x
p1.x = -1
p1.x


'''
A method which is used for getting a value is decorated with @property

A method which has to function as the setter is deecorated with @<function_name>.setter
'''

#BETTER WAY TO use properties

class P:

    def __init__(self, x):
        self.__set_x(x)

    def __get_x(self):
        return self.__x

    def __set_x(self,x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
        

    x = property(__get_x, __set_x)

p1 = P(100)
p1.x
p2 = P(-11)
p2.x

# Each attribute has or should have its own property(or getter-setter pair)
# and the other way aroudn.

class Robot:
    'class definition of the class Robot'

    def __init__(self, name, build_year, lk = 0.5, lp = 0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        
        if s <= -1 :
            return "I feel miserable!"

        elif s <= 0 :
            return "I feel bad!"
        
        elif s <= 0.5:
            return "Could be worse!"
        
        elif s <=1 :
            return "seems to be okay!"
        
        else:
            return "Great!"

x = Robot("Marvin", 1979, 0.2,0.4)
y = Robot("Caliban", 1993, -0.4, 0.3)

print(x.condition)
print(y.condition)

'''Let's say we have the following class definition and usage, where people are using our instance attributes
publicly and now if we are required to add logic to the instance attribute OurAttr without changing the use case.
Solution: Use properties for the attribute OurAttr
'''

class OurClass:
    def __init__(self, x):
        self.OurAttr = x

x = OurClass(-10)
x.OurAttr

# solution

class OurClass:
    '''class definition of the class OurClass'''

    def __init__(self, x):
        '''initializer method'''
        self.OurAttr = x

    @property
    def OurAttr(self):
        return self.__OurAttr

    @OurAttr.setter
    def OurAttr(self, x):
        if x < 0:
            self.__OurAttr = 0
        elif x > 1000:
            self.__OurAttr = 1000
        else:
            self.__OurAttr = x

p1 = OurClass(100)
p2 = OurClass(10001)
p3 = OurClass(-100)
p1.OurAttr
p2.OurAttr
p3.OurAttr

# So we can start with a simple implementation using public instance attribute and then add property to
# it without changing the logic at other places.


'''
first programming language to use object was Simula 67, introduced in 1967.

major breakthrough in oops in the programming language SmallTalk in the 1970s.

the 4 major oop principles:
* Encapsulation
* Data Abstraction
* Polymophism
* Inheritance

'''

'''
In python everything is first-class: integer, string, classes, variables; all are classes,
that means all are equal
'''

x = 42
type(x)

y = 3.1459
type(y)

def f(x):
    return x + 1

type(f)

import math
type(math)

x = [1,2,3]
type(x)

class Robot:
    pass

if __name__ == "__main__":
    x = Robot()
    y = Robot()

    y2 = y

    print(y == y2)
    print(y == x)

'''
properties and attributes are different things in python.
'''

'''
we can dynamically create arbitrary new attributes for existing instances of a class.
'''

x = Robot()
y = Robot()

x.name = "Marvin"
x.build_year = "1979"

y.name = "Jarvis"
y.build_year = "1933"

print(x.name)
print(x.build_year)

'''
The instances possess dictionaries __dict__, which they use to store their attirbutes
and their corresponding values
'''
x.__dict__
y.__dict__


'''Attributes can be bound to class names as well, in this case, each instance will possess
this name as well. But we should be aware when we assign the same name to an instance.'''

class Robot1(object):
    pass

x = Robot1()
Robot1.brand = 'kuka'
x.brand

x.brand = 'Honda'

Robot1.brand
x.brand
y = Robot1()
y.brand

Robot1.brand = 'Thales'
y.brand # when we try to access y.brand, python first checks for 'brand' in y.__dict__, if it is
        # not found then it will for Robot1.__dict__. If it is not found even in the className.__dict__
        # then AttributeError will be raised.
x.brand

'''So the class attributes will be accessible from all instances and when we reassign
the same attribute with a new value for an instance, the instance will bound the attribut
for itself'''

x.__dict__
y.__dict__

Robot1.__dict__

x.energy # This will raise AttributeError since the attribute 'energy' is neither in x.__dict___
        # nor in ClassName.__dict__. Here the ClassName is Robot1.

getattr(x,'energy','No_Attr_energy')
getattr(x,'brand','No_Brand')

''' Even function names can be attributed. We can bind an attribute to a function name in the same way
we have done so far to othe instances of classes. '''

def f(x):
    '''function doc string goes here'''
    return 42

f.y = 100
print(f.y)

dir(f)

for attr_name in dir(f):
    print('attr_name:{} \t value:{}'.format(attr_name, getattr(f,attr_name,"no_value")))


f.__doc__

def f(x):
    f.counter = getattr(f, "counter", 0 ) + 1
    if f.counter % 2 == 0:
        f.isCalledEvenTimes = True
    else:
        f.isCalledEvenTimes = False
    return "Monty Python"

for i in range(10):
    f(i)

print(f.counter)
print(f.isCalledEvenTimes) 

# using the above function attributes technique we can save function related values within the function.
# use cases: function call counter, decision based on number of function calls, maybe on who called the function.


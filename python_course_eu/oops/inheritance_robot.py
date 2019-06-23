'''
Inheritance was invented in 1969 for Simula.
Python supports multiple inheritance.

Inheritance allows programmers to create classes that are built
upon existing classes, and this makes it possible to inherit the
attributes and methods of the parent class.

Inheritance supports code reusability.

The relationships of objects or classes through inheritance
give rise to a directed graph.

base class / Parent class
subclass / Child Class

Superclasses are sometimes called ancestors as well.
'''

class Robot:
    '''class definition of the class Robot'''

    def __init__(self,name):
        self.name = name
    
    def say_hi(self):
        print("Hi, I am "+ self.name)

class PhysicianRobot(Robot):
    pass

x = Robot("Marvin")
y = PhysicianRobot("James")

print(x, type(x))
print(y, type(y))

y.say_hi()

'''
Here the Physician Robot inherits both the say_hi() and __init__ method from
the Robot class.
Inheriting them means that we can use them as if they had been defined in the
PhysicianRobot class.
'''

# diff between type and isinstance function

x = Robot("Marvin")
y = PhysicianRobot("James")

print(isinstance(x, Robot), isinstance(y, Robot))
print(isinstance(x, PhysicianRobot))
print(isinstance(y, PhysicianRobot))
print(type(y) == Robot, type(y) == PhysicianRobot)

# isinstance() returns True if we compare an object either with
# the class it belongs to or with the Superclasses
# whereas the type() equality check returns true only if an object is compared with
# its own class

# example of isinstance()
class A:
    pass

class B(A):
    pass

class C(B):
    pass

x = C()
print(isinstance(x, A))
print(type(x) == A)
print(type(x) == B)
print(type(x) == C)

# Overriding a method in inheritance

class Robot:
    '''class definition of the class Robot'''

    def __init__(self,name):
        self.name = name
    
    def say_hi(self):
        print("Hi, I am "+ self.name)

class PhysicianRobot(Robot):
    def say_hi(self):
        print("Everything will be okay!")
        print(self.name + " takes care of you!")


y = PhysicianRobot('James')
y.say_hi()

'''
A method of a prent class gets overridden by simply defining in 
the child class a method with the same name.
'''

'''
If a method is overriden in a class, the original method can still be accessed,
but we have to do it by calling the method directly with the class name,
i.e. Robot.say_hi(y)
'''

y = PhysicianRobot('Doc James')
y.say_hi()

print('... and now the "traditional" robot way of saying hi ;-)')
Robot.say_hi(y)

# A base class can add it's own new method after inherting from the base class

import random

class Robot:
    'class definition of the class Robot'

    def __init__(self, name):
        'initializer method'
        self.name = name
        self.health_level = random.random()

    def say_hi(self):
        'prints a greeting message'
        print("Hi, I am "+ self.name)

    def needs_a_doctor(self):
        'checks for health_level attribute and returns True/False'
        if self.health_level < 0.8:
            return True
        else:
            return False

class PhysicianRobot(Robot):
    'class definition of the class PhysicianRobot'

    def say_hi(self):
        print("Everything will be okay!")
        print(self.name + " takes care of you!")

    def heal(self,robo):
        robo.health_level = random.uniform(robo.health_level, 1)
        print(robo.name + " has been healed by " + self.name + "!")

doc = PhysicianRobot("Dr. Frankenstein")

rob_list = []

for i in range(5):
    x = Robot("Marvin" + str(i))
    if x.needs_a_doctor():
        print("health level of "+x.name + "before healing:", x.health_level)
        doc.heal(x)
        print("health level of "+x.name + "after healing:", x.health_level)
    
    rob_list.append((x.name, x.health_level))

print(rob_list)

'''
When we override a method, we sometimes want to reuse the methods 
of the parent class and add some new stuff.

By this we reduce redundant code.
'''

class PhysicianRobot(Robot):
    def say_hi(self):
        Robot.say_hi(self) # we can also use super().say_hi()
        print("and I am a physician!")

doc = PhysicianRobot("Dr. Frankenstein")
doc.say_hi()

'''
We can use super keyword to call the methods, but its power is seen
in mutliple inheritance case or when we change the parent class
'''

# distinction between overwriting, overloading and overriding

# OVERWRITING
'''
If we overwrite a function, the original function will be gone.
The function will be redefined. This process has nothing to do 
with object orientation or inheritance.
'''

def f(x):
    return x + 42

print(f(32))

# f will be overwritten(or redefined) in the following:

def f(x):
    return x + 43

print(f(32))


# OVERLOADING

'''
Overloading is not directly connectred to OOP.
Overloading is the ability to define a function with the same
name multiple times.
The definitions are different concerning the number of parameters 
and the type of the parameters.

It is the ability of one function to perform different tasks, depending on the number of
parameters of the types of the parameters.
'''

def successor(x):
    return x + 1

'''
Here we have defined a function successor, but in Python
the argument x is just a reference to an object.
It can be integer, float, or any user-defined class.
So strong class typing is missing.
'''

def f(n):
    return n + 42

def f(n, m):
    return n + m + 42

print(f(3,5))
'''
Here the older f(n) is completely redefined by f(n, m)
so we cannot call f(n) anymore
'''

print(f(4))

'''But we can simulate the overloading behaviour of C++
in Python by using default parameter
'''

def f(n, m=None):
    if m:
        return n + m + 42
    else:
        return n + 42

print(f(3), f(4,5))

# We can use the * operator for varying number of arguments

def f(*x):
    if len(x) == 1:
        return x[0] + 42
    elif len(x) == 2 :
        return x[0]+ x[1] + 42
    elif len(x) == 3 :
        return x[0] + x[1] + x[2] + 42
    
    else:
        return 42

print(f(3))
print(f(1,2))
print(f(1,2,3))
print(f(1,2,3,4,5))

#OVERRIDING
# this is same as the overloading concept in inheritance.
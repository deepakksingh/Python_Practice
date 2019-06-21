'''
Instance attributes are owned by the specific instances of a class.
Class attributes are attributes which are owned by the class itself. They
will be shared by all the instances of the class. Therefore they have the same value for every
instance.
'''
class A:
    'class definition of class A'

    a = 'I am a class attribute!'

x = A()
y = A()

x.a
y.a
A.a

# Note: To change a class attribute we have to use the notation ClassName.AttributeName, if we use
# Object.AttributeName, then it will create a new attribute for the Object.
# This happens because class attributes and object attributes are stored in separate dictionaries.

class A:
    'Class Definition of Class A'

    a = 'I am a class attribute'

x = A()
y = A()
x.a = 'This creates a new instance attribute for x!'
y.a
A.a
A.a = 'This will change the class attribute \'a\''
y.a
x.a
A.a

x.__dict__
A.__dict__
y.__dict__

# To access the dictionary of an object's class
x.__class__.__dict__


# Implementation of instance counter using class attribute

class C:
    'class definition of class C'
    
    counter = 0

    def __init__(self):
        'defintion of __init__ method'
        type(self).counter += 1

    def __del__(self):
        'definition of __del__ method'
        type(self).counter -= 1

if __name__ == "__main__":
    x = C()
    print("Number of instances: " + str(C.counter))
    y = C()
    print("Number of instances: " + str(C.counter))
    del(x)
    print("Number of instances: " + str(C.counter))
    del(y)
    print("Number of instances: " + str(C.counter))

# We can make the class attributes private as well.

class Robot:
    'class definition of class Robot'

    __counter = 0

    def __init__(self):
        'definition for intializer'
        type(self).__counter += 1
    
    def RobotInstances(self):
        return Robot.__counter

if __name__ == "__main__":
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(y.RobotInstances())


Robot.RobotInstances()
# This will raise an error because RobotInstances() method takes object reference

# Now if we drop the self from the RobotInstance() method we can access it as Robot.RobotInstances()
# as shown below

class Robot:
    'class definition of class Robot'
    __counter = 0

    def __init__(self):
        'initializer method definition'
        type(self).__counter += 1
    
    def RobotInstances():
        return Robot.__counter

Robot.RobotInstances()
x = Robot()
x.RobotInstances()

# Now we are not able to call x.RobotInstances() because RobotInstances() doesn't take instance reference

'''
We want a method, which we can call via the class name or via the instance name without the
necessity of passing a reference to an instance to it.
'''

'''
Solution: Use static methods, which don't need a reference to an instance
'''
# We can turn a method into a static method by using the decorator @staticmethod 

class Robot:
    'class defintion of class Robot'

    __counter = 0

    def __init__(self):
        'definition of initializer'
        type(self).__counter +=  1
    
    @staticmethod
    def RobotInstances():
        return Robot.__counter

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(y.RobotInstances())
    print(Robot.RobotInstances())



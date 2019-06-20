def hi(obj):
    print("Hi, I am " + obj.name + "!" )

clas Robot:
    pass

x = Robot()
x.name = "Deepak"
hi(x)

class Robot:
    say_hi = hi

x = Robot()
x.name = "Kumar"
Robot.say_hi(x)
x.say_hi()

'''Method differs from a function only in two aspects:
1.  It belongs to a class, and it is defined within a class
2.  The first parameter in the definition of a method has to be a reference to the instance,
    which called the method. This parameter is usually called 'self'.

'self' is not a python keyword, it's just a naming convention,'''

type(x).say_hi(x)
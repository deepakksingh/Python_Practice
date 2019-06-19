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
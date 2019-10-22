'''
2 different kinds of decorators in python
a) Function decorators
b) Class decorators

A decorator in Python is any callable Python object that is used 
to modify a function or a class.
A reference to a function "func" or a class "C" is passed to a decorator
and the decorator returns a modified function or class.
The modified functions or classes usually contain calls to the original function "func"
or class "C"

'''
# Function names are just references
def succ(x):
    return x + 1

successor = succ
successor(10)
succ(10)

del successor
succ(10)

#Functions inside Functions
#example 1:
def f():
    def g():
        print("Hi, it's me 'g'")
        
    print("Hi, it's me 'f")
    g()

f()

#example 2:
def temperature(t):
    def celsius2fahrenheit(x):
        return 9*x/5 + 32

    result = f"It's {str(celsius2fahrenheit(t))} degrees!"
    return result

print(f"{temperature(20)}")
print("#"*10)
#Functions as parameters:
def g():
    print("Hi, from 'g'")

def f(func):
    print("Hi, from f")
    print(f"Now calling the passed parameter {func.__name__}")
    func()

f(g)

print("#"*10)

#Functions returning Functions
'''
The output of a function is also a reference to an object. Therefore functions can return references to function objects.
'''

def f(x):
    def g(y):
        return y + x + 3
    return g

g1 = f(1)
g2 = f(2)

print(g1(1))
print(g2(2))

print("#"*10)
#Example : polynomial factory
def polynomial_creator(a, b, c):
    def polynomial(x):
        return a*x**2 + b*x + c
    return polynomial

p1 = polynomial_creator(2, 3, 1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(0,10, 1):
    print(x, p1(x), p2(x))

print("#"*10)
#Example : polynomial factory of arbitrary degree

def polynomial_factory(*coefficients):
    '''
    coefficients are of in the order of a_n,..., a_1, a_0
    '''
    def polynomial(x):
        res = 0
        for index, coeff in enumerate(coefficients[::-1]):
            res += coeff*x**index

        return res
    return polynomial

p1 = polynomial_factory(4,1)
print(p1(1))


print("#"*10)
#Example : factorized polynomial factory of arbitrary degree

def factorized_polynomial_factory(*coefficients):
    def polynomial(x):
        res = coefficients[0]
        for i in range(1, len(coefficients)):
            res = res * x + coefficients[i]
        return res
    return polynomial

p1 = factorized_polynomial_factory(4,1)
print(p1(1))

print("#"*10)
'''
A simple decorator
'''
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling: " + func.__name__)
        func(x)
        print("After calling: " + func.__name__)
    
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(40)

print("#"*10)
#The usual syntax for decorators in python
'''
The decoration occurs in the line before the function header.
The '@' is followed by the decorator function name.
'''

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)

    return function_wrapper

@our_decorator
def succ(n):
    return n+1

succ(10)

#we can decorate third party functions, eg. functions we import from a module. WE CAN'T USE THE PYTHON SYNTAX WITH THE @ SIGN IN THIS CASE.

from math import sin, cos
sin = our_decorator(sin)
cos = our_decorator(cos)

for f in [sin,cos]:
    f(3.1415)

'''
We can say that a decorator in python is a callable python object that is used to modify as function, method or class definition. The original
object, the one which is going to be modified, is passed to a decorator as an argument. The decorator returns a modified object.
e.g a modified function, which is bound to the name used in the definition.

'''

print("#"*10)
#A generalized version of the function_wrapper, which accepts functions with arbitrary parameters:

from random import random, randint, choice
def our_decorator(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        res = func(*args, **kwargs)
        print(res)
        print("After calling " + func.__name__)

    return function_wrapper

random = our_decorator(random)
randint = our_decorator(randint)
choice = our_decorator(choice)

random()
randint(3,8)
choice([4,5,6])

print("#"*10)
#Use case of Decorators

#1 Checking Arguments with a Decorator
#The following program uses a decorator function to ensure that the argument passed to the function factorial is a positive integer

def arg_test_natural_number(f):
    def helper(x):
        print("checking for non-negative arguments")
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper

@arg_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

# for i in range(1,10):
#     print(i, factorial(i))

# print(factorial(-1))

print("#"*10)
#2 Counting Function calls with Decoratos
#The following decorator counts the number of times a function has been called, BUT THIS WORKS FOR EXACTLY ONE PARAMETER

def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1

print(succ.calls)
for i in range(10):
    succ(i)

print(succ.calls)

print("#"*10)
#The following decorator counts the number of times a function has been called, BUT THIS WORKS FOR MULTIPLE PARAMETERS
def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls +=1
        return func(*args, **kwargs)

    helper.calls = 0
    return helper

@call_counter
def succ(x):
    return x + 1

@call_counter
def mul1(x, y = 1):
    return x*y + 1

print(succ.calls)
for i in range(10):
    succ(i)

mul1(3,1)
mul1(3,4)
mul1(1,1)

print(succ.calls)
print(mul1.calls)

print("#"*10)

#Decorators with Parameters
def evening_greeting(func):
    def function_wrapper(x):
        print("Good Evening!," + func.__name__)
        func(x)

    return function_wrapper

def morning_greeting(func):
    def function_wrapper(x):
        print("Good Morning!," + func.__name__)
        func(x)

    return function_wrapper

@evening_greeting               #foo = evening_greeting(foo)
def foo(x):
    print(x)

foo("deepak")


'''
Above we have used 2 decorators but only their message changes, we can pass even pass parameter to a decorator to reuse the function
'''

def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(f"{expr}, {func.__name__} returns")
            func(x)
        return function_wrapper
    return greeting_decorator

@greeting("namaste")
def foo(x):
    print(x)

#if we do not want to use the @ decorator syntax, we can do it with function call
def custom_greeting_msg(greet_msg):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(greet_msg)
            func(x)
            
        return function_wrapper
    return greeting_decorator


def foo(x):
    print(x*2)

hola_greeter = custom_greeting_msg("Hola!!!")

foo = hola_greeter(foo)
foo(42)

namaste_greeter = custom_greeting_msg("namaste!!!")
foo = namaste_greeter(foo)
foo(42)

'''
If we have a decorator defined in a different module then the attributes like __name__, __doc__, __module__ will be overridden
To overcome this we have to save the values in the decorator definition itself.
'''
from greeting_decorator import greeting

@greeting
def f(x):
    """just a random function definition"""
    return x*4

f(10)
print(f"function name: {f.__name__}")
print(f"function doc: {f.__doc__}")
print(f"module name: {f.__module__}")

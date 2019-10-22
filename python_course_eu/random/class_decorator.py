'''
We know that a decorator is simply a callable object that takes a function as an input parameter.
A function is a callable object, but there are many other callable objects.

A callable object is an object which can be used and behaves like a function but might not be a function.
It is possible to define classes in a way that the instances will be callable objects.
The __call__ method is called, if the instance is called "like a function", i.e. using brackets.
'''

class A:
    def __init__(self):
        print("An instance of A was initialized")

    def __call__(self, *args, **kwargs):
        print("Arguments are :", args, kwargs)

x = A()

print("Now calling the instance:")
x(3,4, x=11, y=10)
print("Let's call it again")
x(3,4, x=11, y=10)

#defining a Fibonacci sequence generator using only class
class Fibonacci:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0 :
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)

        return self.cache[n]

fib = Fibonacci()

for i in range(15):
    print(fib(i), end = " ")


print("#"*10)

def decorator1(f):
    def helper():
        print("decorating,",f.__name__)
        f()
    return helper

@decorator1
def foo1():
    print("inside foo()")

foo1()

#the above decorator1 can be defined as a class too, shown below
class decorator2:
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("decorating,",self.f.__name__)
        self.f()

@decorator2             #foo = decorator2(foo)
def foo():
    print("inside food()")

foo()

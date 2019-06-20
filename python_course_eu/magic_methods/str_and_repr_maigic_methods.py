l = ["python","java","c++"]
print(l)

str(l)
repr(l)

d = {
    'a' : 3497,
    'b' : 1258
}

print(d)

str(d)
repr(d)

x = 128
print(x)
str(x)
repr(x)

'''If you apply str or repr to an object, Python is looking for a corresponding __str__ or
__repr__ in the class definition of the object. If the method does exist, it will be called.'''

# before and after having __str__ and __repr__ method in a class

class A:
    pass

a = A()
print(a)
print(str(a))
print(repr(a))

'''If a class has a __str__ method, the method will be used for an instance x of that class,
if either the function str is applied  to it or if it is used in a print function.
__str__ will not be used, if repr is called, or if we try to output the value directly'''

class A:
    def __str__(self):
        return "Class A str value"

a = A()

print(repr(a))
print(str(a))
a
print(a)

'''Otherwise, if a class has only the __repr__ method and no __str__ method, __repr__ will be applied
in the situations, where __str__ would be applied, if it were available.'''

class A:
    def __repr__(self):
        return "Class A repr value"

    def __str__(self):
        return "Class A str value"

a = A()
print(repr(a))
print(str(a))
print(a)
a

''' __str__ is always the right choice. if the output should be for the end user, we should use __str__'''

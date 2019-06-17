# def Hello(name="Everybody"):
#     """Greet a person"""

#     print("Hello "+ name + "!") 

# Hello()
# Hello("Deepak")

# print("The docstring of the function Hello:"+ Hello.__doc__)

#######
# def no_return(x, y):
#     c = x + y
#     return

# res = no_return(4, 5)
# print(res)


# local and global variables in functions

# def f():
#     print(s)
#     s = "Perl"
#     print(s)

# s = "Python"
# f()
# print(s)

# 

# def f():
#     global s
#     print(s)
#     s = "dog"
#     print(s)

# s = "cat"
# f()
# print(s)

#
# def arithmetic_mean(first, *values):
#     """This function calculated the arithmetic mean of a non-empty
#     arbitrary number of numerical values"""

#     return (first + sum(values))/(1+len(values))


# print(arithmetic_mean(45,32,89,79))
# print(arithmetic_mean(45))

# x = [1, 2, 3]
# arithmetic_mean(*x)

#

# my_list = [('a', 232),
#             ('b', 343),
#             ('c', 543),
#             ('d', 23)]

# list(zip(*my_list))

#

# def f(**kwargs):
#     print(kwargs)

# f()

# f(de='German', name="deepak", age=26)

def f(a, b, x, y):
    print(a, b, x, y)

d = {'a':'append', 'b': 'block', 'x': 'concatenate', 'y': "decapitate"}
f(**d)


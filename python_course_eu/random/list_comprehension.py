'''
List comprehension is an elegant way to define and create list in Python. These lists have often the qualities of sets,
but are not in all cases sets.

List comprehension is a complete substitute for the lambda function as well as the functions map(), filter(), and reduce().
'''

#example for map() substitute

celsius = [39.2, 36.5, 37.3, 37.8]
fahrenheit = [(float(9)/5*x + 32) for x in celsius]
print(f"{fahrenheit}")

#generating pythogorean triplets
pyt_trips = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]
print(f"{pyt_trips}")

#generating cross-products
colours = ["red", 'green', 'yello', 'blue']
things = ['house', 'car', 'tree']
coloured_things = [(x, y) for x in colours for y in things]
print(f"{coloured_things}")


'''
Generator Comprehension:
    They are simply like a list comprehension but with paranthesis - round brackets - instead of (square)
    brackets around it. 
    The syntax and the way of working is like list comprehension
    NOTE: A generator comprehension returns a generator instead of a list.
'''

x = (x**2 for x in range(20))
print(f"{x}") #prints the generator object

x = list(x)
print(f"{x}")

#Calculation of the prime numbers between 1 and 100 using The Sieve of Erotosthenes
no_primes = [j for i in range(2, 8) for j in range(i*2, 100 ,i)]

primenums = [x for x in range(2, 100) if x not in no_primes]

print(f"{primenums}")


#a more general representation
from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
no_primes = [j for i in range(2, sqrt_n + 1) for j in range(i*2 , n , i)]
print(f"{no_primes}")


#there will be many duplicate entries but they can be removed by using set notation
from math import sqrt
n = 100
sqrt_n = sqrt(n)
no_primes = {j for i in range(2, sqrt_n + 1) for j in range(i*2, n, i)}
no_primes
primes = {i for i in range(2, n) if i not in no_primes}
primes

#NOTE:
'''
In Python2, the loop control variable is not local, i.e. it can change another variable of that name outside
of the list comprehension
'''


x = "Python3 fixed the dirty little secret"
res = [x for x in range(3)]
print(res)
print(x)
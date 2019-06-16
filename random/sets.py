import os

_ = os.system("clear")

# x = set("DEEPAK KUMAR SINGH")
# x
# type(x)
#=======
# list1 = ["India","Australia","England","India"]
# tuple1 = ("India","Australia","England","India")

# set(list1)
# set(tuple1)
#=======

# tuple1 = (("python","perl"),("paris","berlin"),("python","perl"))
# set(tuple1)
# list1 = [["deepak"],["kumar"]]
# set(list1)

# cities = ["bengaluru","hyderabad","gorakhpur"]
# cities = frozenset(cities)
# cities.add("pune")
# cities

#========

# adjectives = {"cheap","expensive","inexpensive","economical"}
# adjectives.add("colorful")
# adjectives
# adjcopy = adjectives
# adjectives.clear()
# adjectives
# adjcopy

#=========

#set_difference
# x = {'a','b','c','d','e'}
# y = {'b','c'}
# z = {'a','d'}
# x.difference(y).difference(z)
# x-y-z

#difference_update
# x.difference_update(y)

# x = x - y
# x

#discard
# x = {'a','b','c','d','e'}
# x.discard('k')
# x

#remove
# x = {'a','b','c','d','e'}
# x.remove('g')
# x


#union(s) and intersections(s)
# x = {'a','b','c','d','e',1}
# y = {'c','e','f','j'}
# z = {1,2,3,'z'}
# x.union(y).union(z)
# x | y
# x.intersection(y)
# x & y

#isdisjoint()

# x = {'a','b','c'}
# y = {'c','d','e'}
# z = {1,2,3}
# x.isdisjoint(y)
# x.isdisjoint(z)

#issubset()
# x= {'a','b','c','d','e'}
# y = {'c','d'}
# x.issubset(y)
# x <= y
# y.issubset(x)
# y <= x

# x < y

# y < x

# x < x

#issuperset()
# x= {'a','b','c','d','e'}
# y = {'c','d'}

# x.issuperset(y)
# x >= y
# y.issuperset(x)
# y >= x

# x > x
# x.issuperset(x)

#pop()
# str = "abcdefghijklmnopqrstuvwxyz"
# strlist = list(str)
# strlist
# x = set(strlist)
# for i in range(len(x)):
#     print(x.pop())
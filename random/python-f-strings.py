'''contains various ways of formatting a string'''
name = 'Deepak'
place = 'Hyderabad'
print("Hello, I'm {} and I live in {}".format(name,place))

# We can reference variables in any order by referencing their index
print("I live in {1}, and my name is {0}".format(name,place))

# We can also refer the variables with names

person = {
    'name' : 'Deepak',
    'place' : 'Hyderabad',
}

print("My name is {name} and I live in {place}".format(**person))

'''
str.format() is much more easily readable than code using %-formatting, but str.format()
can still be quite verbose when we are dealing with mutliple parameters and longer strings
'''

person = {
    'name': 'Deepak',
    'place' : 'Hyderabad',
    'from' : 2019,
    'profession': 'MS'
}
print("Hello I'm {name}, I live in {place} where I'm doing my {profession} since {from}".format(**person))

# Using f-strings
# also called as formatted string literals

'''
f-strings are string literals that have an f at the beginning and curly braces containing expression that will
be replaced with their values.
The expressions are evaluated at runtime and then formatted using the __format__ protocol.
'''
name = "Deepak"
place = "Hyderabad"

f"Hello, I'm {name}, I live in {place}"
F"Hello, I'm {name}, I live in {place}"

# Becuase f-strings are evaluated at runtime, we can put any and all valid Python expressions in them.
f"{2*37}"

def to_uppercase(input):
    return input.upper()

name = "Deepak Kumar Singh"

f"{to_uppercase(name)}"
f"{name.upper()}"

# We can use f-strings in classes

class Comedian:
    '''class definition of class Comedian'''

    def __init__(self, first_name, last_name, age):
        '''initializer method'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!!!"

new_comedian = Comedian("Deepak","Singh",26)
f"{new_comedian}"


# NOTE: By default, f-strings will use __str__(), but we can make sure they use __repr__()
# in including the conversion flag !r

f"{new_comedian!r}"

# Multiline f-strings
name = "Eric"
profession = 'comedian'
affiliation = 'Monty Python'

message = (
    f"Hi {name}."
    f"You are a {profession}"
    f"YOU WERE IN {affiliation}"
)
message

# for multiline f-strings to work we have to place an f in each line

message = (
    f"Hi {name}."
    "You are a {profession}"
    "You were in {affiliation}."
)
message

# we can also use line-breaks for multiline f-strings
message =   f"Hi {name}." \
            f"You are a {profession}." \
            f"You were in {affiliation}."

message

#If we use """ we get this
message = f'''
        Hi{name}.
        You are a {profession}.
        You were in {affiliation}.
        '''
message

'''
f-strings are faster than both %-formatting and str.format().
f-strings are expressions evaluated at runtime rather than constant values.
'''

comedian = {
    'name' : 'Eric Idle',
    'age': 74
}

f"The comedian is {comedian['name']}, aged {comedian['age']}'"

# To introduce braces to appear in your string, you must use double braces

f"{{74}}"

f"{{{74}}}"

f"{{{{74}}}}"

# Expressions should not include comments using the # symbol
f"Eric is {2*37 #Oh my!}."
'''
An exception is an eror that happens during the execution of a program, it implies that the problem(the exception) doesn't occur frequently.
Error handling is generally resolved by saving the state of execution at the moment the error occurred and interrupting the normal
flow of the program to execute a special function or piece of code, which is known as the exception handler.
The error handler can "fix" the problem and the program can be continued afterwards with the previously saved data.
'''
#Exception handling in python
'''
THe code, which harbours the risk of an exception, is embedded in a try block. But whereas in Java exceptions are caught by catch clauses, we have statements
introduces by an 'except' keyword in Python.
It's possible to create 'custom-made' exceptions: with the raise statement it's possible to force a specified exception to occur.
'''

n = int(input("Please enter a number:"))
#the above line will raise a ValueError if we enter non-integer numbers

#using exception handling
try:
    n = input("Enter an integer:")
    n = int(n)
    print(n)

except ValueError:
    print(" Not a Valid integer!")

#NOTE:
'''
A try statement may have more than one except clause for different exceptions, But at most one except clause
will be executed
'''

import sys

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())

except IOError as e:
    errno, strerror = e.args
    print(f"I/O Error ({errno}):({strerror})")
    print(f"{e}")
except ValueError as e:
    print(f"No valid integer in line.")
except:
    print(f"Unexpected error: {sys.exc_info()[0]}")
    raise


#demonstrating exception inside a function

def f():
    x = int("four")

try:
    f()
except ValueError as e:
    print("caught the exception :)", e)

print("move on")

#in the above code snipped, the exception is handled outside the function

#to handle the exception inside the function

def f():
    try:
        x = int("four")
    except ValueError as e:
        print("got it in the function :) as ", e)
        raise  #propagates the error the caller

try:
    f()
except ValueError as e:
    print("this will be  printed too", e)

print("Let's get on")


#Custom made exceptions
raise SyntaxError("Sorry, my fault!")

class MyException(Exception):
    pass

raise MyException("An exception doesn't always prove the rule!")



#Clean-up Actions
'''
The try statement can be followed by a finally clause.
Finally clause are called clean-up or termination clauses, because they must be executed under all circumstances,
i.e. a "finally" clause is always executed regardless if an exception occurred in a try block or not.
'''


try:
    x = float(input("Your number:"))
    inverse = 1.0 / x
finally:
    print("There may or may not have been an exception.")

print("The inverse:", inverse)


#combining try, except, and finally

try:
    x = float(input("Your number:"))
    inverse = 1.0 / x
except ValueError as e:
    print("You should have not given either an int or a float")
except ZeroDivisionError as e:
    print("Infinity")
finally:
    print("There may or may not have been an exception")


#ELSE Clause
'''
The try..except statement has an optional else clause. An else block has to be positioned after all the except clauses.
An else clause will be executed if the try clause doesn't raise an exception
'''

import sys
file_name = "integers.txt"
text = []

try:
    fh = open(file_name, 'r')
    text = fh.readlines()

except IOError as e:
    print(f"Cannot open file", e)

finally:
    fh.close()

if text:
    print(text[100])


#usage of else block
import sys
file_name = "./integers.txt"
text = None

try:
    fh = open(file_name, 'r')
except IOError:
    print("cannot open", file_name)
else:
    text = fh.readlines()
    fh.close()

if text:
    print(text[100])
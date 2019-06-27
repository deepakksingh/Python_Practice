'''
Multiple inheritance is a feature in which a class can inherit attributes and
methods from more than once parent class.

Multiple inheritance suffers from 'Diamond problem'

Example:
CalendarClock class will inherit from both the Calendar class and Clock class.
So that we can use both the functionality in the same class.
'''

class Clock(object):
    '''This class simulates a clock'''

    def __init__(self, hours, minutes, seconds):
        '''
        The parameters hours, minutes and seconds
        have to be integers and must satisfy the following equations:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        '''
        self.set_clock(hours, minutes, seconds)

    def set_clock(self, hours, minutes, seconds):
        '''sets the clock parameter values'''

        if type(hours) == int and 0 <= hours and hours < 24:
            self._hours = hours
        else:
            raise TypeError("Hours have to be integers between 0 and 23!")

        if type(minutes) == int and 0 <= minutes and hours < 60:
            self._minutes = minutes
        else:
            raise TypeError("Minutes have to be integers between 0 and 59!")

        if type(seconds) == int and 0 <= seconds and seconds < 60:
            self._seconds = seconds
        else:
            raise TypeError("Seconds have to be integers between 0 and 59!")    

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self._hours, self._minutes, self._seconds)

    def tick(self):
        '''
        This method lets the clock "tick", this means that the internal time will 
        be advanced by one seconds.
        '''

        if self._seconds == 59:
            self._seconds = 0
            if self._minutes == 59:
                self._minutes = 0
                if self._hours == 23:
                    self._hours = 0
                else:
                    self._hours += 1
            else:
                self._minutes += 1
        else:
            self._seconds += 1

x = Clock(23,59,59)
print(x)
x.tick()
print(x)
y = str(x)
print(type(y))

x = Clock(7.7,2,2)
x = Clock(7,5,80)

class Calendar(object):
    '''This class implements a calendar.'''
    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    date_style = "British"

    @staticmethod
    def leapyear(year):
        '''
        The method leapyear returns True if the parameter year is a 
        leap year, False otherwise
        '''

        if not year % 4 == 0 :
            return False
        elif not year % 100 == 0:
            return True
        elif not year % 400 == 0:
            return False
        else:
            return True

    def __init__(self, d, m, y):
        ''' d, m, y have to be integer values and year has to be a four digit year number'''
        self.set_calendar(d, m, y)

    def set_calendar(self, d, m, y):
        if type(d) == int and type(m) == int and type(y) == int:
            self.__days = d
            self.__months = m
            self.__years = y
        else:
            raise TypeError("d, m, y have to be integers")

    def __str__(self):
        if Calendar.date_style == "British":
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__days, self.__months, self.__years)
        else:
            #assuming American style
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__months, self.__days, self.__years)


    def advance(self):
        '''This method advances to the next date'''
        max_days = Calendar.months[self.__months - 1]

        if self.__months == 2 and Calendar.leapyear(self.__years):
            max_days += 1

        if self.__days == max_days:
            self.__days = 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            
            else:
                self.__months += 1
        else:
            self.__days += 1


x = Calendar(31,12,2012)
print(x)
x.advance()
print(x)

x = Calendar(28, 2, 2012)
print(x)
x.advance()
print(x)

x = Calendar(28, 2, 2013)
print(x)
x.advance()
print(x)

Calendar.date_style = "American"
print(x)

# Now the multiple inheritance example of CalendarClock begins

class CalendarClock(Clock, Calendar):
    '''
    The class CalendarClock implements a clock with integrated calendar.
    It's a case of multiple inheritance, as it inherits both the Clock and Calendar
    '''

    def __init__(self, day, month, year, hours, minutes, second):
        Clock.__init__(self, hours, minutes, second)
        Calendar.__init__(self, day, month, year)

    def tick(self):
        '''
        advance the clock by one second
        '''
        previous_hour = self._hours
        Clock.tick(self)
        if(self._hours < previous_hour):
            self.advance()

    def __str__(self):
        return Calendar.__str__(self) + ", " + Clock.__str__(self)

x = CalendarClock(31,12,2013,23,59,59)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)

x = CalendarClock(28,2,1900,23,59,59)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)

x = CalendarClock(28,2,2000,23,59,59)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)

x = CalendarClock(7,2,2013,13,55,40)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)


'''
The "diamond problem" is the generally used term for an ambiguity
that arises when 2 classes B and C inherit from a superclass A, and the other class D inherits
from both B and C. If there is a method "m" in A that B or C (or even both of them) has overridden,
and furthermore, if does not override this method, then the question is which version of the mthod does D
inherit?
It could be the one from A, B or C.
'''

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")

class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    pass

d = D()
d.m()       # this will print 'm of B called'


# AMBIGUITIES
class A:
    def m(self):
        print("m of A called")

class B(A):
    pass
    
class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    pass

x = D()
x.m()

class D(C, B):
    pass
d = D()
d.m()       # this will print 'm of C called'

'''
Multiple inheritance with old-style classes is governed by two rules:
depth-first and then left-to-right (Method-Resolution-Order)
If we change the header line of class A to "class A(object):", we will have the same behavior in both 
python 2 and python 3 versions.
'''


class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")

class C(A):
    def m(self):
        print("m of C called")

class D(B, C):
    def m(self):
        print("m of D called")

x = D()
x.m()
B.m(x)
C.m(x)
A.m(x)

# If we want the method m of D to execute the code of m of B, C and A as well, we do it as follows.
class D(B, C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)
        A.m(self)

x = D()
x.m()

# But if the class B and C also call A.m(self) in their m() method, the result will be as follows:

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
        A.m(self)

class C(A):
    def m(self):
        print("m of C called")
        A.m(self)

class D(B, C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)

x = D()
x.m()

# Solution: split the methods m of B and C in 2 methods.
'''
The first method, called _m consists of the specific code for B and C and the other method is still called
m, but consists now of a call self._m() and a call A.m(self). Now m of D consists of the calls B._m(self)
C._m(self) and A.m(self).
'''

class A:
    def m(self):
        print("m of A called")

class B(A):
    def _m(self):
        print("m of B called")
    
    def m(self):
        self._m()
        A.m(self)

class C(A):
    def _m(self):
        print("m of C called")
    
    def m(self):
        self._m()
        A.m(self)

class D(B, C):
    def m(self):
        print("m of D called")
        B._m(self)
        C._m(self)
        A.m(self)


x = D()
x.m()
# The above solution works but it's not an elegant solution.

# The optimal way to solve the problem, which is the "super" pythonic way, consists
# of calling the super function

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
        super().m()

class C(A):
    def m(self):
        print("m of C called")
        super().m()

class D(B, C):
    def m(self):
        print("m of D called")
        super().m()

x = D()
x.m()

'''
The super function is often used when instances are initialized with the __init__ method
'''

class A:
    def __init__(self):
        print("A.__init__")

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()

d = D()
c = C()
b = B()
a = A()

'''
But how does the super function decide which class has to be used?
It resolves it using MRO-Method Resolution Order.
MRO : based on the "C3 superclass linearisation" algorithm
This is called as linearisation, because the tree structure is broken down into a linear order.
'''
D.mro()
C.mro()
B.mro()
A.mro()


# Polymorphism
'''
The ability to present the same interface for differing underlying forms.
Polymorphic functions or methods can be applied to arguments of different types, and they can behave
differently depending on the type of the arguments to which they are applied.
We can also define the same function with a varying number of parameters.
'''

def f(x, y):
    print("values:", x, y)

f(42, 43)
f(43.5,60)

'''
Here we can call f(...) with various types of arguments but in a typed programming language like
Java of C++, we would have to overload f to implement the various type combinations.
'''

# NOTE: python is implicity polymorphic.
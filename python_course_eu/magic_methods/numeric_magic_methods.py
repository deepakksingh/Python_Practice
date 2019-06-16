import math
class MyNumber(int):

    #unary operators
    def __pos__(self):
        """Implement behavior for unary positive"""
        print("Unary + operator called.")
        return self
    
    def __neg__(self):
        """Implement behavior for unary negative"""
        print("Unary - operator called.")
        return self
    
    def __abs__(self):
        """Implement behavior for the built in abs() function"""
        print("unary operator abs() called")
        return self

    def __invert__(self):
        """Implement behavior for the ~ operator"""
        print("bitwise negation operator called")
        return self
    
    def __round__(self,n):
        """Implement the behavior for the built-in round() function and n is the number of decimals
        places to round to"""
        print("round() function called")
        return self

    def __floor__(self):
        """Implement the behavior for math.floor() ;  rounding down to the nearest integer"""
        print("math.floor() is called")
        return self
    
    def __ceil__(self):
        """Implement the behavior for math.ceil() ; rounding up to the nearest integer"""
        print("math.ceil() is called")
        return self

    def __trunc(self):
        """Implement the behavior for math.trunc() ; truncating to an integral"""
        print("math.trunc() is called")
        return self


    #binary operators
    def __add__(self,other):
        """Implement the behavior for + operator"""
        print("binary + operator called")
        return self



x = MyNumber(2)
x
-x
from functools import wraps
def greeting(func):
    @wraps(func)  #INSTEAD OF MANUALLY UPDATING THE ATTRIBUTES, the wraps decorator of functools does this in the background
    def function_wrapper(x):
        """function wrapper of greeting"""
        print(f"Hi, {func.__name__}")
        return func(x)

    # function_wrapper.__name__ = func.__name__
    # function_wrapper.__doc__ = func.__doc__
    # function_wrapper.__module__ = func.__module__
    return function_wrapper
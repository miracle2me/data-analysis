from functools import wraps

def logged(func):
    @wraps(func)
    def with_logging(*args,**kwargs):
        print func.__name__+' was called'
        return func(*args,**kwargs)
    return with_logging

@logged
def f(x):
    """does some math"""
    return x + x * x

f(3)
print f.__name__
print f.__doc__

# without @wraps, the print is:
"""
f was called
with_logging
None
"""

# with @wraps, the print is:
"""
f was called
f
does some math
"""

# order of decorator
"""
@staticmathod、@classmethod、@property

@a
@b
@c
def f ():

equal to :
f = a(b(c(f)))


"""
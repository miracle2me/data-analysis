# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("  after myfunc() called.")
#     return func

def deco(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("  after myfunc() called.")
    return _deco

@deco
def myfunc():
    print(" myfunc() called.")
    return "OK"


myfunc()
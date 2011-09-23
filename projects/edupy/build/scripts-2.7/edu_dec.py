#!C:\Python27\python.exe
class Some_Decorator(object):

    def __init__(self, f):
        print "inside some decorator init"
        # calls the function being decorated    
        f()

    # need to make the class callable to use it as a decorator
    def __call__(self):
        print "inside decorator.call()"


# using a class as decorator
@Some_Decorator
def some_function():
    print "inside some function"




some_function()




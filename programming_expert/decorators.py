def decorators(func):
    def abc(x):
        print("welcome to my first decorator function")
        func(x)
    return abc

@decorators
def hello_decarator(x):
    print("hello decorator", x)

hello_decarator(10)
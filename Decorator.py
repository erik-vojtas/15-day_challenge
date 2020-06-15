# Decorators
# • Python has an interesting feature called decorators to add functionality to an existing code.
# • This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time
# • A decorator in Python is an object that takes a function and returns a function.

def my_decorator(f):
    def f1():
        print ("before hello")
        f()
        print ("after hello")
    return f1

@my_decorator
def hello():
    print("hello")

hello()
print("-------------------------")


def my_decorator(f):
    def f1(*args, **kwargs):
        print ("before ")
        f(*args, **kwargs)
        print ("after ")
    return f1

@my_decorator
def fy(t):
    print(t)

@my_decorator
def fx(t, name="silly"):
    print(t, name)

fx(10)
fy(20)
print("-------------------------")


# • Write a Python Decorator called @isGreater10, which when applied to a function checks whether the return value of that function is greater than 10
# • If the return value is greater than 10, it prints “Hurray”.
#
def isGreater10(funct):
    def wrappedUpFunct():
        if funct() > 10:
            print("Hurray!!!")
        else:
            print("Your number is smaller or equal to 10")
    return wrappedUpFunct


@isGreater10
def somecalculation1():
    # complex stuff here
    return 2

@isGreater10
def somecalculation2():
    # complex stuff here
    return 12

somecalculation1()
somecalculation2()
print("-------------------------")


class Execute_3_times:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        self.function()
        self.function()
        self.function()

# adding decorator to the class
@Execute_3_times
def function():
    print("Hello")

print (type(function))
function()

print("-------------------------")

# Define three decorators so that the the output of the method mp() is altered:
# • @boldaddsthe<b>..</b>tag
# • @italic<i>..</i>tag
# • @unterline<u>..</u>tag

def bold(f):
    def wrappedUpFunct():
        return f"<b>{f()}</b>"
    return wrappedUpFunct

def italic(f):
    def wrappedUpFunct():
        return f"<i>{f()}</i>"
    return wrappedUpFunct

def underline(f):
    def wrappedUpFunct():
        return f"<u>{f()}</u>"
    return wrappedUpFunct



# @bold
# @italic
# @underline

@underline
@italic
@bold
def mp():
    return "hello world"

print(mp())

print("-------------------------")

def isGreater100(fn):
    def wrapperFunct(num):
        if fn(num) < 100:
            print("smaller or equal to 100")
        else:
            print("bigger than 100")
    return wrapperFunct

@isGreater100
def somecalculation(num):
    # complex stuff here
    return num

somecalculation(200)
print("-------------------------")
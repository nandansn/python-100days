## Web server

## Flask

- framework to implement service in the python
- need to install flask library
- use Flask() class initate the server
- use python decorator for routing the request like @app.route('/')


### python decorator 

- A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.
- Basically, a decorator takes in a function, adds some functionality and returns it.


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

pretty = make_pretty(ordinary)
pretty()

**Output**
I got decorated
I am ordinary

- you can create decorators for paramterized functions

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


- you can chain the decorators

- Multiple decorators can be chained in Python.

- This is to say, a function can be decorated multiple times with different (or same) decorators. We simply place the decorators above the desired function.

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
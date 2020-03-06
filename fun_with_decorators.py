#!/usr/bin/env python
from functools import wraps

def silly(original_function):

    @wraps(original_function)
    def imposter(*args, **kwargs):
        print("in imposter:", args, kwargs)
        print("Beware the decorator!")
        return original_function(*args, **kwargs)

    return imposter

@silly
def spam(a, **kw):
    print("Hello from spam")

@silly
def ham(a, b, **kw):
    print("Hello from ham")

spam("wombat", animal='gorilla')
spam("weevil", filename='foo.txt')
ham(1, 5)
print(spam.__name__)
print(ham.__name__)


@foo('abc')
def bar():
    pass

bar = foo('abc')(bar)

x`


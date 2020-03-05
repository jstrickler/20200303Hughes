#!/usr/bin/env python

def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)
spam('a', 'b', 'c')

my_args = ['red', 'white', 'blue']
spam(*my_args)


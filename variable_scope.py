#!/usr/bin/env python
import sys
# def print(*args):
#     sys.stdout.write("HA HA HA!\n")

x = 100  # GLOBAL variable

def spam():
    cave_man = 'ogg'  # LOCAL variable
    print(cave_man, x)

spam()

print("x is", x)
# print("cave man is", cave_man)

def spam():
    x = 5  # NESTED scope  from POV of ham()
    def ham():
        print(x)
    return ham

h = spam()
h()

#!/usr/bin/env python
"""
Enthralling example module for the above-average
students at Hughes
"""

import typing as T

Numeric = T.Union[int, float]

def spam(x: Numeric, y: Numeric) -> float:
    """
    The spectacular spam() function in
    all its glory.

    :param x: A number
    :param y: Another number
    :return: Some number based on x and y
    """
    return x * y

print(spam(1.2, 3.4))
print(spam('abc', 5))

print(spam.__annotations__)

# spam.color = 'blue'
# print(spam.color)
print()
print(spam.__doc__)

print(spam(45, 1.8))

def hello(whom="world"):
    print("Hello", whom)

hello("world")
hello("Mom")
hello("Hughes")
hello()






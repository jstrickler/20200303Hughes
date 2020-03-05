#!/usr/bin/env python
from itertools import zip_longest

d1 = dict()  # new, empty dict
d2 = {'a': 5, 'm': 17, 'wombat': ('Australia', 'Marsupial')}
d3 = {}

things = [('a', 5), ('m', 17), ('c', 8)]
d4 = dict(things)
print(d4)

keys = ['a', 'c', 'm', 'v', 'r']
d = dict(zip_longest(keys, [], fillvalue=0))
print(d)

values = [5, 8, 9, 10]
print(list(zip(keys, values)))
d2 = dict(zip(keys, values))
print(d2)

my_list = list(zip(keys, values))
my_tuple = tuple(zip(keys, values))
print(my_list)
print(my_tuple)

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

fruit_info = {f.lower(): len(f) for f in fruits}
print(fruit_info, '\n')

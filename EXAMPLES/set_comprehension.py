#!/usr/bin/env python

import re

with open("../DATA/parrot.txt") as mary_in:
    s = {w.lower()  for ln in mary_in  for w in re.split(r'\W+', ln)} #<1>
print(s)

foods = ['spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam',
        'toast', 'eggs', 'bacon',
        'tofu', 'jackfruit',
    'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', ]

unique_foods = set(foods)
print(unique_foods)

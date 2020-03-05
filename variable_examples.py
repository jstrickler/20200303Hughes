#!/usr/bin/env python

x = 5
y = x

x = 10

print(x, y)

y = 20
m = 20

data = [1, 2, 3]
x = data
x.append(42)
print(data, x)

a = b = []
print(id(a), id(b))
a.append("huh?")
print(a, b)
b.append("what the heck?")
print(a, b)

data = [1, 2, 3, ['spam', 'ham']]
a = data  # alias, not copy
b = list(data)  # shallow copy
b[-1].append("toast")
b[0] = "PYTHON IS GREAT!"

print("data:", data)
print("a:", a)
print("b:", b)
import copy
c = copy.deepcopy(data) # deep copy
c[-1].append("eggs")
print("data:", data)
print("c:", c)

values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

print(values[-100000:1000000])


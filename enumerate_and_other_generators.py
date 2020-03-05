#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple"]

e = enumerate(fruits)
print(e)

for i, fruit in e:
    print(i, fruit)
print()


# SORT OF writing C in python
i = 0
for fruit in fruits:
    print(i, fruit)
    i += 1
print()

# for (i = 0; i < sizeof(fruits); i++) {
#     printf("%d %s", i, fruits[i])
# }

e = enumerate(fruits)
print(next(e))
print(next(e))
print(next(e))


i = iter(fruits)
print(next(i))
print(next(i))


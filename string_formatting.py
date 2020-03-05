#!/usr/bin/env python


cave_man = "ogg"

home = "cave"

n = 838023.93093930

thing = 'rutabaga'

print(cave_man, n, thing)

print(cave_man, n, thing, sep=", ")

print(cave_man, n, thing, sep="")

print(cave_man, n, thing, sep="%")

print(cave_man)
print(n)
print(thing)
print('=' * 10)
print(cave_man, end="/")
print(n, end='%')
print(thing)

print(cave_man, 'lives in', home)

print("{} lives in {}".format(cave_man, home))

print("%s lives in %s" % (cave_man, home))

print("value is {:.2f}".format(n))
print("value is %.2f" % (n))


print(f"{cave_man} lives in {home}")


print(f"value is {n:.2f}")


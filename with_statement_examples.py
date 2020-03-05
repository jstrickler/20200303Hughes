#!/usr/bin/env python

with open('DATA/mary.txt') as file_in:
    print(file_in.closed)
    for line in file_in:
        print(line, end='')

print(file_in.closed)



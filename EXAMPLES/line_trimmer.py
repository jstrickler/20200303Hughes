#!/usr/bin/env python

with open('../DATA/mary.txt') as mary_in:
    for line in mary_in:
        print(line, end='')
print('-' * 60)

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            if line.endswith('\n'):
                line = line.rstrip('\n\r')
            yield line  # <1>

file_gen = trimmed('../DATA/mary.txt')
for trimmed_line in file_gen:  # <2>
    print(trimmed_line)

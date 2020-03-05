#!/usr/bin/env python

with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip() # remove \n
        # ...

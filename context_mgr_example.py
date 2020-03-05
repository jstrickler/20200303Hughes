#!/usr/bin/env python

class Thing:
    def __init__(self):
        print("New instance!")

    def __enter__(self, *args):
        print("Entering:", args)
        return self

    def __exit__(self, *args):
        print("Exiting:", args)

with Thing():
    # print("t is", t)
    print("Doing something.....")


with open('DATA/mary.txt') as mary_in:
    pass






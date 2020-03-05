#!/usr/bin/env python

def main():
    spam()
    ham()
    spam()

def spam():
    _toast()
    print("spam!")

def ham():
    print("Ham!!")

def _toast():
    print("I'm in toast!")

if __name__ == '__main__':
    main()

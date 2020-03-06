#!/usr/bin/env python

import timeit

setup_code = """from hughes.tech.hugheslib import spam, ham"""

codes = [
    '''ham()''',
    '''spam()''',
]

for code in codes:
    t = timeit.Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit(10000))
    print()


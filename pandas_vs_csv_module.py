#!/usr/bin/env python
import timeit

setup_code = """
import pandas as pd
import csv
FILE = 'DATA/baby-names.csv'
"""

codes = [
    '''
df = pd.read_csv(FILE)
    ''',
    '''
with open(FILE) as file_in:
    rdr = csv.reader(file_in)
    rows = list(rdr)
    ''',
]

for code in codes:
    t = timeit.Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit(100))
    print()


#!/usr/bin/env python
import pandas as pd
import csv
from pprint import pprint

knight_data = {}

with open('DATA/knights.csv') as knights_in:
    next(knights_in)
    rdr = csv.reader(knights_in)
    for row in rdr:
        name = row.pop(0)
        title = row.pop(0)
        if name not in knight_data:
            knight_data[name] = row

pprint(knight_data)


df = pd.read_csv("DATA/knights.csv", skiprows=1, names=['name', 'title', 'color', 'quest', 'comment', 'number', 'ladies'])

print(df)
print(df.describe())
print(df.info())
print(df.loc[0])
print(df['name'][0])
print(df['name'][1])

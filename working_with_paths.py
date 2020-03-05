#!/usr/bin/env python
import os  # also imports os.path
from datetime import datetime

FILE = 'alice.txt'
FOLDER = 'DATA'

file_path = os.path.join(FOLDER, FILE)
print("file path:", file_path)

print(os.path.exists(file_path))

print(os.listdir(FOLDER), '\n')

file_size = os.path.getsize(file_path)
print("file size:", file_size)

basename = os.path.basename(file_path)
dirname = os.path.dirname(file_path)
abspath = os.path.abspath(file_path)
print("base:", basename)
print("dir:", dirname)
print("absolute path:", abspath)

print(os.path.isfile(file_path))
print(os.path.isdir(file_path))
print(os.path.isfile(FOLDER))
print(os.path.isdir(FOLDER))
print(os.path.splitext(file_path))

raw_mod_time = os.path.getmtime(file_path)
print("raw mod time:", raw_mod_time)

mod_time = datetime.fromtimestamp(raw_mod_time)
print("mod time:", mod_time)


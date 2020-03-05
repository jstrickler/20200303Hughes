#!/usr/bin/env python
import os

#  os.walk()

start_dir = "."
# start_dir = os.path.abspath(start_dir)

biggest = None, 0

for dir_path, subs, files in os.walk(start_dir):
    print(dir_path)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            if file_size > biggest[1]:
                biggest = file_path, file_size
            print("{:8d} {}".format(file_size, file_name))

print("biggest:", biggest)

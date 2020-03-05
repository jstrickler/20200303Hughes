#!/usr/bin/env python
import os
from datetime import datetime
import time

start_date = datetime(2019, 1, 1)
end_date = datetime(2019, 12, 31)

start_tuple = start_date.timetuple()
end_tuple = end_date.timetuple()

start_epoch = time.mktime(start_tuple)
end_epoch= time.mktime(end_tuple)

start_dir = "/Users/jstrick/py/DATA"
# start_dir = os.path.abspath(start_dir)

for dir_path, subs, files in os.walk(start_dir):
    for file_name in files:
        file_path = os.path.join(dir_path, file_name)
        file_timestamp = os.path.getmtime(file_path)
        if start_epoch <= file_timestamp <= end_epoch:
            print(file_path, datetime.fromtimestamp(file_timestamp))

print(datetime.)

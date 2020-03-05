#!/usr/bin/env python

from datetime import datetime, date, timedelta

print("date.today():", date.today())  # <1>

now = datetime.now()  # <2>
print("now.day:", now.day)  # <3>
print("now.month:", now.month)
print("now.year:", now.year)
print("now.hour:", now.hour)
print("now.minute:", now.minute)
print("now.second:", now.second)

d1 = datetime(2018, 6, 13)  # <4>
d2 = datetime(2018, 8, 24)

d3 = d2 - d1  # <5>

print("raw time delta:", d3)
print("time delta days:", d3.days)  # <6>

interval = timedelta(10, 10, 5)  # <7>
print("interval:", interval)
print(interval.days, interval.seconds, interval.microseconds)


d4 = d2 + interval  # <8>
d5 = d2 - interval
print("d2 + interval:", d4)
print("d2 - interval:", d5)
print()

t1 = datetime(2016, 8, 24, 10, 4, 34)  # <9>
t2 = datetime(2018, 8, 24, 22, 8, 1)
t3 = t2 - t1

print("datetime(2016, 8, 24, 10, 4, 34):", t1)
print("datetime(2018, 8, 24, 22, 8, 1):", t2)
print("time diff (t2 - t1):", t3)

result = d1 + timedelta(7, 60 * 60 * 12)
print(result)

#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(person[0], person[1])
print(len(person))
print(person[:2])

first_name, last_name, product, dob = person

values = 'a', 'b', 'c', 'd', 'e', 'f'

i, j, *k = values
print(i, j, k)
i, *j, k = values
print(i, j, k)
*i, j, k = values
print(i, j, k)
print()

for v in values:
    # v, x = next(values)
    print(v)
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]

for first_name, last_name, *_, dob in people:
    print(first_name, last_name, dob)
print('-' * 60)


#        0     1    2    3     4     5    6
values = 'a', 'b', 'c', "c'", 'd', 'e', 'f'

for i, v in enumerate(values):
    print(i, v)

print(list(enumerate(values)))

x = 1, 5, "thing"

for i, v in enumerate(x):
    print(i, v)


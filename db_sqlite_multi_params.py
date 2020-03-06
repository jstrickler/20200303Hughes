#!/usr/bin/env python


import sqlite3

with sqlite3.connect("DATA/presidents.db") as s3conn:
    s3cursor = s3conn.cursor()

    party_query = '''
    select firstname, lastname
    from presidents
        where party = ? and birthstate == ?
    '''  # <1>


    param_lists = [
        ('Republican', 'Illinois'),
        ('Democratic', 'Arkansas'),
        ('Democratic', 'Hawaii'),
    ]

    for param_list in param_lists:
        s3cursor.execute(party_query, param_list)
        print(param_list)
        for row in s3cursor.fetchall():
            print(row)
        print()



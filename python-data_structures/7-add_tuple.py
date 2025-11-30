#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        x = tuple_a[0]
        y = tuple_a[1]
    elif len(tuple_a) == 1:
        x = tuple_a[0]
        y = 0
    else:
        x = 0
        y = 0
    if len(tuple_b) >= 2:
        m = tuple_b[0]
        n = tuple_b[1]
    elif len(tuple_b) == 1:
        m = tuple_b[0]
        n = 0
    else:
        m = 0
        n = 0
    c = x + m
    d = y + n
    new_tuple = (c, d)
    return new_tuple

#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        x = sorted(my_list)
        y = x[-1]
        return y

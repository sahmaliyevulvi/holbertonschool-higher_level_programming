#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    sett = set_1.union(set_2)
    new_set = set(sett)
    for i in set_1:
        for j in set_2:
            if i == j:
                new_set.remove(i)
    return new_set

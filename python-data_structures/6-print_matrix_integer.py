#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('')
    for a in matrix:
        for b in range(len(a)):
            if b != len(a) - 1:
                print("{:d}".format(a[b]), end=' ')
            elif b == len(a) - 1:
                print("{:d}".format(a[b]), end="\n")

#!/usr/bin/python3
"""Defines the MyList class that inherits from list."""


class MyList(list):
    """A class that inherits from list."""

    def __init__(self):
        self.res = []

    def print_sorted(self):

        for i in self:
            if i > 0:
                self.res.append(i)

        print(sorted(self.res))

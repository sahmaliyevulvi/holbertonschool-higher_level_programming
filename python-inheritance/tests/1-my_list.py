#!/usr/bin/python3
"""Defines the MyList class that inherits from list."""


class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original."""
        print(sorted(self))

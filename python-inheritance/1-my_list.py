#!/usr/bin/python3
"""Defines the MyList class that inherits from list."""


class MyList(list):
    """Custom list class that extends list."""

    def print_sorted(self):
        """Prints the list but sorted in ascending order."""
        print(sorted(self))

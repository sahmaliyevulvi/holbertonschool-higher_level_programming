#!/usr/bin/python3
"""Function that returns True if the object is an instance of,
or inherited from, a class"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass,
otherwise False"""
    return isinstance(obj, a_class)

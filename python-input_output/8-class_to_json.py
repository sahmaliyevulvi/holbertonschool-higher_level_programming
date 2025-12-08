#!/usr/bin/python3
"""Module that defines a function
to convert a class instance to a dictionary"""


def class_to_json(obj):
    """Returns the dictionary description of
    an object for JSON serialization"""
    return obj.__dict__

#!/usr/bin/python3
"""Module that defines a function to load
a Python object from a JSON file"""


import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

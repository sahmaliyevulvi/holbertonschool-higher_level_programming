#!/usr/bin/python3
"""Module that defines a function to read and print a text file"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

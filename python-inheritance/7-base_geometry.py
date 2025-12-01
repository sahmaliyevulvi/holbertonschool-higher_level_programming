#!/usr/bin/python3
"""Defines BaseGeometry class with area() and integer_validator() methods"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

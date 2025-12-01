#!/usr/bin/python3
"""Defines BaseGeometry class with unimplemented area method"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception because area is not implemented"""
        raise Exception("area() is not implemented")

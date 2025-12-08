#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dict representation of Student.
        If attrs is a list of strings, return only those attributes.
        """
        if (
            isinstance(attrs, list)
            and all(isinstance(a, str) for a in attrs)
        ):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        using the key-value pairs in `json`.
        """
        for key, value in json.items():
            setattr(self, key, value)

#!/usr/bin/python3
"""
Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square with size validated by BaseGeometry
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """String representation of the square"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

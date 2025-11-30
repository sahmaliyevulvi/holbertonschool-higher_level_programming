#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, v):
        if not isinstance(v, int):
            raise TypeError("width must be an integer")
        if v < 0:
            raise ValueError("width must be >= 0")
        self.__width = v

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, v):
        if not isinstance(v, int):
            raise TypeError("height must be an integer")
        if v < 0:
            raise ValueError("height must be >= 0")
        self.__height = v

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        s = str(self.print_symbol)
        return "\n".join(s * self.__width for _ in range(self.__height))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(r1, r2):
        if not isinstance(r1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(r2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return r1 if r1.area() >= r2.area() else r2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

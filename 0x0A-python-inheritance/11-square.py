#!/usr/bin/python3
"""Definition of a Rectangle Square"""



Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square from Rectangle class"""

    def __init__(self, size):
        """This initializes a Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """This Returns a string with area"""
        return super().area()

    def __str__(self):
        """This returns a printable string """
        return "[Square] {}/{}".format(self.__size, self.__size)

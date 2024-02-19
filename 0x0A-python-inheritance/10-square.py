#!/usr/bin/python3
"""Definition of Rectangle Subclass square"""



Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the Square from Rectangle class"""
    def __init__(self, size):
        """Initializes a new Square"""
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)
        self.__size = size

    def area(self):
        """Returns a string with area"""
        return super().area()

#!/usr/bin/python3
"""Definition of a class from BaseGeometry"""



BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle with BaseGeometry Class"""

    def __init__(self, width, height):
        """Initializes new Rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

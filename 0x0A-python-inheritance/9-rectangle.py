#!/usr/bin/python3
"""DEfinition of Rectangle that inherits BaseGeometry"""



BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle from BaseGeometry Class """

    def __init__(self, width, height):
        """Initializes Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method that will return area of the instance"""
        return self.__width * self.__height

    def __str__(self):
        """Special method that returns string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

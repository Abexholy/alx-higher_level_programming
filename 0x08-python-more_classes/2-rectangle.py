#!/usr/bin/python3
"""Defines a Rectangle Class."""


class Rectangle:
    """This Represents a Rectangle."""

    def __init__(self, width=0, height=0):
        """This is a Method that will initialize the instance

        Args:
            width: The rectangle width
            height: The rectangle height


        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Set that returns the value of the width

        Returns:
            rectangle width


        """

        return self.__width

    @width.setter
    def width(self, value):
        """This is method that defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero


        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculates the Rectangle area

        Returns:
            rectangle area


        """

        return self.width * self.height

    def perimeter(self):
        """Return perimeter of Rectangle."""

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

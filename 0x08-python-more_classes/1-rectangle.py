#!/usr/bin/python3
"""

The module is by a class that defines Rectangle


"""


class Rectangle:
    """Represents a rectangle """

    def __init__(self, width=0, height=0):
        """This initializes the instance

        Args:
            width (int): width of the new rectangle.
            height (int): height of the rectangle.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width rectange."""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set the returns and the value of the height

        Returns:
            height of the rectangle


        """

        return self.__height

    @height.setter
    def height(self, value):
        """This Defines the Value

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

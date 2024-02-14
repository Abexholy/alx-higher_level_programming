#!/usr/bin/python3
"""This initialize a Rectangle"""


class Rectangle:
    """ Class will defines a rectangle """

    def __init__(self, width=0, height=0):
        """Method to initialize instance """

        self.width = width
        self.height = height

    @property
    def width(self):
        """This is the method that returns the value of the width

        Returns:
            rectangle width

        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("The width must be an integer")
        if value < 0:
            raise ValueError("The width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This will set the hight of Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This is will calculate Rectangle area

        Returns:
            rectangle area

        """

        return (self.__width * self.__height)

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """This Returns the Rectangle #

        Represents rectangle with the # character
        """


        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for j in range(self.__height):
            [rect.append('#') for i in range(self.__width)]
            if j != self.__height -1:
                rect.append("\n")
        return ("".join(rect))

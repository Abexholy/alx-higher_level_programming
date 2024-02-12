#!/usr/bin/python3
"""Define a Rectangle"""


class Rectangle:
    """Defines a rectangle """

    def __init__(self, width=0, height=0):
        """This initializes the Rectangle

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of the Rectangle.

        Returns:
            rectangle width


        """

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
        """This is a method that returns the value of the height

        Returns:
            rectangle height


        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This Method calculates the Rectangle area

        Returns:
            rectangle area


        """

        return self.width * self.height

    def perimeter(self):
        """This method will calculate the Rectangle perimeter

        Returns:
            rectangle perimeter


        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for j in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """Return the string rep of rectangle. """

        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

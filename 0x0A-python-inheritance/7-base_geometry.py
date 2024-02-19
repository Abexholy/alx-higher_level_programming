#!/usr/bin/python3
"""Definition to base geometry class"""


class BaseGeometry:
    """The Geometry Shapes"""

    def area(self):
        """Defines the area of a geomtric shape"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This will recieve the value property integer

        Árgs:
            name (str): name of the object or parameter
            value (int): value to validate.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

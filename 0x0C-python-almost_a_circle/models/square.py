#!/usr/bin/python3
"""Definition of all square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a Class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """This will Initialize new instances

        Args :
            size : The Size of new square
            x : The x coordinate of the new square
            y : The y coordinate of the new square
            id : the identity of the new square
            """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The str special method """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh

    @property
    def size(self):
        """ Getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def __str__(self):
        """ str special method """
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
        """The new update method """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for j in range(len(args)):
                if list_atr[j] == 'size':
                    setattr(self, 'width', args[j])
                    setattr(self, 'height', args[j])
                else:
                    setattr(self, list_atr[j], args[j])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """This Returns dictionary with it attributes """
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for mau in list_atr:
            if mau == 'size':
                dict_res[mau] = getattr(self, 'width')
            else:
                dict_res[mau] = getattr(self, mau)

        return dict_res

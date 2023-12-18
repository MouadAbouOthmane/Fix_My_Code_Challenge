#!/usr/bin/python3
"""1. My square"""


class square():
    """square class"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Constuctor """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ The perimeter of a square """
        return self.width * 4

    def __str__(self):
        """ String representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

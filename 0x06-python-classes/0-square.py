#!/usr/bin/python3

"""Define a class Square."""


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

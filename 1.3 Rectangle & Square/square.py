from shape import *


class Square(Shape):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def area(self):
        return self.size * self.size

    def __str__(self):
        return f"Size: {self.size}"
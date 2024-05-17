#!/usr/bin/python3

'''
    Write a class Square that defines a square by: (based on 4-square.py)

    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be a number (float or integer), otherwise raise a TypeError exception with the message size must be a number
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Instantiation with size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current square area
    Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area
    You are not allowed to import any module
'''
class Square:

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    # @staticmethod
    def area(self):
        return (self._size * self._size)
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if type(value) is not int or type(value) is not float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def __eq__(self, value):
        return self.area() == value.area()
    def __ne__(self, value):
        return self.area() != value.area()
    def __ge__(self, value):
        return self.area() >= value.area()
    def __le__(self, value):
        return self.area() <= value.area()
    def __lt__(self, value):
        return self.area() < value.area()
    def __gt__(self, value):
        return self.area() > value.area()
    

if __name__ == '__main__':

    my_square = Square(2)
    print(int(my_square.area))

    
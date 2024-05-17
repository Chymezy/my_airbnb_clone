#!/usr/bin/python3

'''
    Write a class Square that defines a square by: (based on 5-square.py)

    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Private instance attribute: position:
    property def position(self): to retrieve it
    property setter def position(self, value): to set it:
    position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
    Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self): that returns the current square area
    Public instance method: def my_print(self): that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line
    position should be use by using space - Don’t fill lines by spaces when position[1] > 0
    You are not allowed to import any module
'''
class Square:

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
        self._position = position
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self._position = value

    # @staticmethod
    def area(self):
        return (self._size ** 2)
    

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value
    
    def my_print(self):
        if self.size == 0:
            print()
        width = self.size
        for i in range(width):
            print('#' * width)

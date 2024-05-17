#!/usr/bin/python3

'''
    Write a class Square that defines a square by: (based on 4-square.py)
    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current square area
    Public instance method: def my_print(self): that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line
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
        
    
# if __name__ == '__main__':
#     s = Square(10)
#     s.my_print()
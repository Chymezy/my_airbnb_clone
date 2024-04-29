import unittest

""" 
baseModel unit testing file
"""
class Test_BaseModel(unittest.TestCase):
    """"
    1. test if class is as basemodel
    2. test if id attr. is an istance of BaseModel
    3. test id is of type str
    4. check if created_at attr. is same as updated_at
    5  check if created_at and updated_at is of iso-time format

    1. test if __str__() returns required format.

    1. test if update_at attr changed when save method is called
    
    1. test if self.__dict__ is same as value of obj attr*
    2. test if __class__ is same as __dict__ key.
    3. test if created_at and update_at aligns to iso time format
    """


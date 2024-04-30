import unittest
from models import BaseModel
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
        
    obj = BaseModel()

    def test_BaseModel_Class(self):
        ''' test if class is basemodel '''
        self.assertIsInstance(obj, BaseModel)

    def test_obj_id(self):
        ''' test if id attr is a field of BaseModel instance '''
        self.assertIsInstance(obj.id, BaseModel)

    def test_objId_str(self):
        ''' test obj id if it is str '''
        self.assertIsInstance(obj.id, str)

    def test_obj_created_at_updated_at(self):
        ''' test obj created_at and updated_at if same '''
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_isoformat(self):
        ''' test created_at attr time format '''
        self.assertEqual(obj.created_at, '%Y-%m-%dT%H:%M:%S.%f')
        self.assertEqual(obj.updated_at, '%Y-%m-%dT%H:%M:%S.%f')

    def test_str(self):
        ''' test str output '''
        self.assertEqual(str(obj),"[self.__class__.__name__] (self.id) self.__dict__ ")

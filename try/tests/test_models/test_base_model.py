#!/bin/bash/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

""" This a test-suite for basemodel class """

class Test_BaseModel(unittest.TestCase):
    def test_obj_creation(self):
        ''' test the created instance attributes and data formating '''
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertTrue(datetime.fromisoformat(obj.created_at.isoformat()))
        self.assertTrue(datetime.fromisoformat(obj.updated_at.isoformat()))
        self.assertIsInstance(obj, BaseModel)
    
    def test_obj_str(self):
        ''' tests the string formating if it matches required output '''
        obj = BaseModel()
        expected_str = f'[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}'
        self.assertEqual(str(obj), expected_str)

    def test_obj_to_dict_serialization(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        i = 0
        for key, value in obj_dict.items():
            i += 1
            self.assertEqual(value, obj.id)
            self.assertTrue(type(value), str)
            if i == 2:
                self.assertEqual(value, obj.created_at)
                self.assertTrue(type(value), datetime.datetime) 


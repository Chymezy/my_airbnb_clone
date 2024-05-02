#!/bin/bash/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

""" This a test-suite for basemodel class """

class Test_BaseModel(unittest.TestCase):
    def test_obj_creation(self):
        obj = BaseModel()
        self.assertTrue(obj.id)
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertTrue(datetime.fromisoformat(obj.created_at.isoformat()))
        self.assertTrue(datetime.fromisoformat(obj.updated_at.isoformat()))
        self.assertIsInstance(obj, BaseModel)
    
    def test_obj_str(self):
        obj = BaseModel()
        expected_str = f'[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}'
        self.assertEqual(str(obj), expected_str)


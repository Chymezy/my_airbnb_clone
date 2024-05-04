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
        expected_str = f'[{obj.__class__.__name__}], ({obj.id}), {obj.__dict__}'
        self.assertEqual(str(obj), expected_str)

    def test_obj_to_dict_serialization(self):
        obj = BaseModel()
        obj_dict = obj.to_dict().copy()
        attr_toCheck = []
        for key in obj_dict.keys():
            attr_toCheck.append(key)
        for attr in attr_toCheck:
            self.assertIn(attr, obj_dict, f'{attr} is missing')
            self.assertIsInstance(attr, str, f'{attr} not instance of str')
            if attr in ['created_at', 'updated_at']:
                self.assertIsInstance(obj_dict[attr], str, f'{attr} is of different type')
                self.assertEqual(obj_dict[attr], getattr(obj, attr).isoformat(), f'{attr} has incorrect format or value')
               #self.assertEqual(obj_dict[attr].isoformat, getattr(obj, attr).isoformat(), f' has incorrect format or value')
            elif attr == '__class__':
                self.assertEqual(obj_dict[attr], obj.__class__.__name__, f'__class__ has incorrect value')
            else:
                self.assertEqual(obj_dict[attr], getattr(obj, attr), f'{attr} has incorrect value')

    def test_save(self):
        ''' test if instance are saved adequately '''
        obj = BaseModel(name='First model')
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)
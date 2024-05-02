#!/bin/bash/python3

import json
from models.base_model import BaseModel
import os
from models import storage

''' This a test cases for file storage class '''
class Test_FileStorage(unittest.TestCase):
    
    def test_all(self):
        ''' test if all stored obj are retrieved '''
        obj = BaseModel(name='First Model')
        storage.new(obj)
        storage.save()
        self.assertIsInstance(obj, storage.__objects[obj])
         

    

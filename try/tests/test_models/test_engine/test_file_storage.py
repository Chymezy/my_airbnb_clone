#!/bin/bash/python3

import json
import unittest
from models.base_model import BaseModel
import os
from models import storage

''' This a test cases for file storage class '''
class Test_FileStorage(unittest.TestCase):
    
    def test_all(self):
        ''' test if all stored obj are retrieved '''
        obj = BaseModel(name='First Model')
        obj.save()
        print(obj.id)
        #self.assertIn(obj.id, storage.all())
         

    

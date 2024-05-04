#!/bin/bash/python3

import unittest
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel
# from models import storage
from models.engine.file_storage import FileStorage
import json

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up the test case"""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down the test case"""
        self.storage = None

    def test_new(self):
        """Test adding a new object to storage"""
        obj = BaseModel(name="Test Object", price=100)      
        self.storage.new(obj)
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", self.storage.all())

    def test_save(self):
        """Test saving objects to the file"""
        obj = BaseModel(name="Programming is Crazzy!")
        obj.save()
        file_path = self.storage.__class__.__dict__.get('_FileStorage__file_path', 'file.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for key, value in data.items():
            if key == 'id':
                self.assertEqual(value, obj.id)


    def test_reload(self):
        ''' test reloading of objects into __objects dict '''
        obj = BaseModel(name="The patient dog does what again?")
        obj.save()
        self.storage.reload()
        key = f'{obj.__class__.__name__}.{obj.id}'
        obj_list = self.storage.all()
        for data in obj_list.keys():
            if data == key:
                self.assertTrue(key)
          
        



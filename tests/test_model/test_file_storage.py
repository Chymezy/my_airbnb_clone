import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.obj1_key = "{}.{}".format(self.obj1.__class__.__name__, self.obj1.id)
        self.obj2_key = "{}.{}".format(self.obj2.__class__.__name__, self.obj2.id)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        self.assertEqual(self.storage.all(), {})
        self.storage.new(self.obj1)
        self.storage.new(self.obj2)
        self.assertEqual(self.storage.all(), {self.obj1_key: self.obj1, self.obj2_key: self.obj2})

    def test_new(self):
        self.storage.new(self.obj1)
        self.assertIn(self.obj1_key, self.storage.all())
        self.assertEqual(self.storage.all()[self.obj1_key], self.obj1)

    def test_save_reload(self):
        self.storage.new(self.obj1)
        self.storage.new(self.obj2)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(self.obj1_key, self.storage.all())
        self.assertIn(self.obj2_key, self.storage.all())
        self.assertEqual(self.storage.all()[self.obj1_key].to_dict(), self.obj1.to_dict())
        self.assertEqual(self.storage.all()[self.obj2_key].to_dict(), self.obj2.to_dict())

if __name__ == "__main__":
    unittest.main()

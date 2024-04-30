import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_instance_of_base_model(self):
        """
        Test if the class is an instance of BaseModel.
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_id_is_string(self):
        """
        Test if the id attribute is an instance of str.
        """
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_id_is_string(self):
        """
        Test if the id attribute is of type str.
        """
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at_equals_updated_at(self):
        """
        Test if created_at equals updated_at.
        """
        model = BaseModel()
        self.assertEqual(model.created_at, model.updated_at)

    def test_created_at_iso_format(self):
        """
        Test if created_at and updated_at are in ISO format.
        """
        model = BaseModel()
        self.assertTrue(datetime.fromisoformat(model.created_at.isoformat()))
        self.assertTrue(datetime.fromisoformat(model.updated_at.isoformat()))

    def test_str_method(self):
        """
        Test if __str__() returns the required format.
        """
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_updated_at_changes_on_save(self):
        """
        Test if updated_at changes when save() method is called.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """
        Test if to_dict() method returns expected values.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()


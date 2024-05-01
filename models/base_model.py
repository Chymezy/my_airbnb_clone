"""Base model module.

This module defines the BaseModel class, which serves as the base class for all other model classes.
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """BaseModel class for other model classes to inherit from."""
    
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance.

        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        self.id = str(uuid.uuid4())
        current_time = datetime.utcnow()
        self.created_at = current_time
        self.updated_at = current_time

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:      
            # Add a call to the method new(self) on storage
            models.storage.new(self)

    def save(self):
        """Save BaseModel instance.

        Updates the updated_at attribute with the current datetime and saves the object to the storage.
        """
        self.updated_at = datetime.utcnow()

        # Call save(self) method of storage
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance.

        Returns:
            dict: Dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

if __name__ == "__main__":
    all_objs = models.storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
    print(models.storage.all())

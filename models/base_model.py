"""Base model module.

This module defines the BaseModel class, which serves as the base class for all other model classes.
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """BaseModel class for other model classes to inherit from."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance.

        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:      
            self.id = str(uuid.uuid4())
            current_time = datetime.utcnow()
            self.created_at = current_time
            self.updated_at = current_time

            # Add a call to the method new(self) on storage
            storage.new(self)

    def save(self):
        """Save BaseModel instance.

        Updates the updated_at attribute with the current datetime and saves the object to the storage.
        """
        self.updated_at = datetime.utcnow()

        # Call save(self) method of storage
        storage.save()

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

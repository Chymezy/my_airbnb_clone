#!/bin/bash/python3

import uuid
from datetime import datetime

class BaseModel:
    ''' root class upon other models inherit from '''
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
    
    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

if __name__ == "__main__":
    obj = BaseModel(name="First Model")
    print(f'name: {obj.name}, \tcreated: {obj.created_at}, \tupdated: {obj.updated_at}')
    print(obj)


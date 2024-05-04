#!/bin/bash/python3

import uuid
from datetime import datetime
import models 

class BaseModel:
    ''' root class upon other models inherit from '''

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

        models.storage.new(self)
    
    def __str__(self):
        ''' formats instance output '''
        return f'[{self.__class__.__name__}], ({self.id}), {self.__dict__}'

    def save(self):
        ''' saves creation and modification of instances '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' serilizes objects to dictionary '''
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj

# if __name__ == "__main__":
#     obj = BaseModel(name="Benjamin Model")
#     # print(f'name: {obj.name}, \tcreated: {obj.created_at}, \tupdated: {obj.updated_at}')
#     # holder = obj.to_dict()
#     # i = 0
#     # for key, value in holder.items():
#     #     i += 1
#     #     print(f'{type(value)}')
#     # print("loop count:", i)
#     # print(obj.id)
#     obj.save()

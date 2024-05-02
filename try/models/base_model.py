
import uuid
from datetime import datetime

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
    
    def __str__(self):
        ''' formats instance output '''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        ''' saves creation and modification of instances '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' serilizes objects to dictionary '''
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at
        obj['updated_at'] = self.updated_at
        return obj

if __name__ == "__main__":
    obj = BaseModel(name="First Model")
    print(f'name: {obj.name}, \tcreated: {obj.created_at}, \tupdated: {obj.updated_at}')
    print(obj)
    for key, value in obj.items():
        print(f'{obj[key]}: {obj[value]}')



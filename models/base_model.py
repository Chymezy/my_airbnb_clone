#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
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


    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

if __name__ == "__main__":
        
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    # print(my_model.id)
    # print(my_model)
    # print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    # print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))
    print("--")
    my_model_json2 = my_new_model.to_dict()
    print("JSON jos_model:")
    for key in my_model_json2.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json2[key]), my_model_json2[key]))

    print("--")
    print(my_model is my_new_model)

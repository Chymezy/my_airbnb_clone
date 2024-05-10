#!/usr/bin/python3
"""
This module represents the `console` (CLI)
Current file: console.py
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

my_list = []
# obj = BaseModel(name="Grace")
# obj.save()
datas = storage.all()
for key, value in datas.items():
    # info = 
    print(value.to_dict())
    print('key: ', key)
    # print('values: ', value)
# print(my_list)
print(datas)
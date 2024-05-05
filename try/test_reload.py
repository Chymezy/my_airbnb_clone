#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
checks = '7c57982e-9312-40d4-b9c9-99731cd140d2'
ids = []
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    ids.append(obj_id.split('.')[1])
    # obj = all_objs[obj_id]
    # print(obj
if checks in ids:
    print("I found it")
# print(ids)

# print("-- Create a new object --")
# my_model = BaseModel()
# my_model.name = "My_First_Model"
# my_model.my_number = 89
# my_model.save()
# print(my_model)
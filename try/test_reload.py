# #!/usr/bin/python3
# """
# This module represents the `console` (CLI)
# Current file: console.py
# """
# import cmd
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
# from models import storage

# my_list = []
# # obj = BaseModel(name="Grace")
# # obj.save()
# datas = storage.all()
# for key, value in datas.items():
#     # info = 
#     print(value.to_dict())
#     print('key: ', key)
#     # print('values: ', value)
# # print(my_list)
# print(datas)
# arg = F'BaseModel.update("6ea6fdc3-4040-4aa7-bb4e-82924ddc43dd", "name", "today")'
# arg1 = arg.split('.')
# obj_id, attr, attr_value = arg1[1][7:-1].split(',')
# print(f'{obj_id} {attr} {attr_value}')

arg = BaseModel.update("6ea6fdc3-4040-4aa7-bb4e-82924ddc43dd", "name", "today")
arg1 = arg.split('.')
# obj_id, attr, attr_value = arg1[1][7:-1].split(',')
# result = obj_id.strip() + ' ' + attr.strip() + ' ' + attr_value.strip()
print(arg1)

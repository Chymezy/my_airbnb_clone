#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a copy of the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to __objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    # def save(self):
    #     """Serializes __objects to the JSON file (path: __file_path)."""
    #     serialized_objs = {}
    #     for key, obj in self.__objects.items():
    #         serialized_objs[key] = obj.to_dict()
    #     with open(self.__file_path, 'w') as f:
    #         json.dump(serialized_objs, f, indent=2)
    
    def save(self):
        """ serializes __objects to JSON file i.e file.json """
        stored_objects = FileStorage.__objects
        serialized_obj_dicts = {}

        for obj in stored_objects.keys():
            serialized_obj_dicts[obj] = stored_objects[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_obj_dicts, file, indent=2)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                try:
                    stored_objects = json.load(file)
                    for key, value in stored_objects.items():
                        class_name, obj_id = key.split(".")
                        obj_class = globals().get(class_name)
                        if obj_class:
                            self.__objects[key] = obj_class(**value)
                except Exception as e:
                    print("Error reloading objects from JSON file:", e)
if __name__ == "__main__":
    store = FileStorage()
    print(store.all())
    print("------")
   # Create instances of your model classes
    obj1 = BaseModel(name="Car-model", price=2300)
    obj2 = BaseModel(name="Bike-model", price=2100)
    obj3 = BaseModel(name="train-model", price=5200)

    # Add the objects to the FileStorage
    store.new(obj1)
    store.new(obj2)
    store.new(obj3)

    #Print the stored objects
    print(store.all())

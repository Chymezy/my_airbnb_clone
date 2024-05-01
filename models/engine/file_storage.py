#!/usr/bin/python3

import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a copy of the dictionary __objects."""
        return self.__objects.copy()

    def new(self, obj):
        """Adds a new object to __objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

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
import json
import os
from models.base_model import BaseModel
''' This the storage model '''

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' return all objects stored in __objects attr '''
        return self.__objects

    
    def new(self, obj):
        ''' adds new instance to stored object dict using class & id '''
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj
    
    
    def save(self):
        ''' serializes instance dict to json and store in a file '''
        stored_obj = self.__objects
        serialized_obj = {}

        for obj in stored_obj.keys():
            serialized_obj[obj] = stored_obj[obj].to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_obj, file, indent=2)

        
    def reload(self):
        ''' deserializes json file into object dict '''
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                try:
                    stored_obj = json.load(file)
                    for key, value in stored_obj.items():
                        class_name, id = key.split('.')
                        obj_class =  globals().get(class_name)  # Assuming models is the package containing all model classes
                        if obj_class:
                            obj_instance = obj_class(**value)
                            self.__objects[key] = obj_instance
                except Exception as e:
                    print("Error reloading objects from JSON file:", e)

    

if __name__ == '__main__':
    store = FileStorage()
    print(store.all())

    obj1 = BaseModel(name="Air-Craft", price=2809)
 

    store.new(obj1)


    print(store.all())
    store.save()
    store.reload()
    print(store.all())

                





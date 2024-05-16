#!/usr/bin/python3 
'''
file module
'''


import json
class FileStorage:
    '''
    file storage class
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        return __objects
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        adds to __objects
        '''
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    def save(self):
        '''
        serializes __objects to the JSON file (path: __file_path)
        '''
        serialized_objs = {}
        for key, obj in  FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w",encoding="utf-8") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''
        try:
            with open(FileStorage.__file_path , "r") as f:
                data = json.load(f)
                from models.base_model import BaseModel
                from models.user import User
                for key, value in data.items():
                    cls, ins_id = key.split(".")
                    obj_dict = value
                    if cls == "BaseModel":
                        obj = BaseModel(**obj_dict)
                    elif cls == "User":
                        obj = User(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

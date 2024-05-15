#!/usr/bin/python3 
'''
file module
'''


import json
class FileStorage:
    '''
    file storage class
    '''
    __file_path = "models/engine/file.json"
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
        saves json into file
        '''
        serialized_objs = {}
        for key, obj in  FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w",encoding="utf-8") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        '''
        realod json from file , convert to dict
        '''
        try:
            with open(FileStorage.__file_path , "r") as f:
                data = json.load(f)
                from models.base_model import BaseModel
                for key, value in data.items():
                    obj_dict = value
                    obj = BaseModel(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

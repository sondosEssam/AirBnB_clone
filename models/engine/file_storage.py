#!/usr/bin/python3
'''
filestorage  module , used to serilize/desirlize objects
'''
import json
import os


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
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''
        if (os.path.exists(FileStorage.__file_path) and
                os.path.getsize(FileStorage.__file_path) == 0):
            return
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                from models.base_model import BaseModel
                from models.user import User
                from models.amenity import Amenity
                from models.city import City
                from models.place import Place
                from models.review import Review
                from models.state import State
                classes = {
                            "BaseModel": BaseModel,
                            "User": User,
                            "Amenity": Amenity,
                            "City": City,
                            "Place": Place,
                            "Review": Review,
                            "State": State
                        }
                for key, value in data.items():
                    cls, ins_id = key.split(".")
                    obj_dict = value
                    if cls in classes:
                        obj_class = classes[cls]
                        obj = obj_class(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

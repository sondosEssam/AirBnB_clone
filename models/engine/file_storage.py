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
        adds to __objecta
        '''
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()
    def save(self):
        '''
        saves json into file
        '''
        with open(FileStorage.__file_path, "w",encoding="utf-8") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        '''
        realod json from file , convert to dict
        '''
        try:
            with open(FileStorage.__file_path , "r") as f:
                FileStorage.__objects = json.load(f.read())
        except Exception:
            pass

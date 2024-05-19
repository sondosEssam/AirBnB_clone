#!/usr/bin/python3
"""
base_class module
contains base class for all other class - parent class
"""


import uuid
import datetime
from models import storage


class BaseModel:
    '''
    BaseModel class - parent class for all other classses
    '''

    def __init__(self, *args, **kwargs):
        '''
        intiating basemodel instance
        '''
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.fromisoformat(value)
                        setattr(self, key, value)
                    else:
                        setattr(self, key, value)

    def __str__(self):
        '''
        representation of basemodel
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        update time
        '''
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        '''
        returns dictionary representation of the class
        '''
        my_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at":
                iso_dt = self.created_at.isoformat()
                my_dict[key] = iso_dt
            elif key == "updated_at":
                iso_dt = self.updated_at.isoformat()
                my_dict[key] = iso_dt
            else:
                my_dict[key] = value
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

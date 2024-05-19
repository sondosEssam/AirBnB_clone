#!/usr/bin/python3
'''
review class that inherits from BaseModel - not used yet
'''


from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Public class attributes
    '''
    place_id = ""
    user_id = ""
    text = ""

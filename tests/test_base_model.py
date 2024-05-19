#!/usr/bin/python3
'''
unittest module for BaseClass
'''
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    '''
    test cases for BaseModel methods
    '''

    def test_init_NoKwargs(self):
        '''
        testing constructor without kwargs
        '''
        with patch('models.storage.new') as mock_storage_new:
            obj = BaseModel()
            self.assertIsInstance(obj, BaseModel)
            self.assertTrue(hasattr(obj, "id"))
            self.assertTrue(hasattr(obj, "created_at"))
            self.assertTrue(hasattr(obj, "updated_at"))
            self.assertEqual(obj.created_at, obj.updated_at)
            mock_storage_new.assert_called_once_with(obj)

    def test_init_kwargs(self):
        '''
        testing constructor with kwargs
        '''
        kwargs = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "name": "testing"
        }
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, kwargs["id"])
        self.assertEqual(obj.created_at, datetime.fromisoformat(kwargs["created_at"]))
        self.assertEqual(obj.updated_at, datetime.fromisoformat(kwargs["updated_at"]))
        self.assertEqual(obj.name, kwargs["name"])

    def test_str(self):
        '''
        testing printing object in required format
        '''
        obj = BaseModel()
        excpected = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), excpected)

    def test_save(self):
        '''
        testing saving objects
        '''
        obj = BaseModel()
        old_update = obj.updated_at
        with patch('models.storage.save') as mock_storage_save:
            obj.save()
            self.assertNotEqual(old_update, obj.updated_at)
            self.assertTrue(obj.updated_at > old_update)
            mock_storage_save.assert_called_once()

    def test_to_dict(self):
        '''
        testing to_dict method
        '''
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())
        self.assertNotIn("name", obj_dict)

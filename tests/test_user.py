#!/usr/bin/python3
'''
unittest module for User class
'''
import unittest
from unittest.mock import patch
from models.user import User
from datetime import datetime
import uuid


class TestUser(unittest.TestCase):
    '''
    test cases for User methods and attributes
    '''

    def test_init_NoKwargs(self):
        '''
        testing constructor without kwargs
        '''
        with patch('models.storage.new') as mock_storage_new:
            obj = User()
            self.assertIsInstance(obj, User)
            self.assertTrue(hasattr(obj, "id"))
            self.assertTrue(hasattr(obj, "created_at"))
            self.assertTrue(hasattr(obj, "updated_at"))
            self.assertTrue(hasattr(obj, "email"))
            self.assertTrue(hasattr(obj, "password"))
            self.assertTrue(hasattr(obj, "first_name"))
            self.assertTrue(hasattr(obj, "last_name"))
            self.assertEqual(obj.email, "")
            self.assertEqual(obj.password, "")
            self.assertEqual(obj.first_name, "")
            self.assertEqual(obj.last_name, "")
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
            "email": "test@example.com",
            "password": "testpassword",
            "first_name": "Test",
            "last_name": "User"
        }
        obj = User(**kwargs)
        self.assertEqual(obj.id, kwargs["id"])
        self.assertEqual(obj.created_at,
                         datetime.fromisoformat(kwargs["created_at"]))
        self.assertEqual(obj.updated_at,
                         datetime.fromisoformat(kwargs["updated_at"]))
        self.assertEqual(obj.email, kwargs["email"])
        self.assertEqual(obj.password, kwargs["password"])
        self.assertEqual(obj.first_name, kwargs["first_name"])
        self.assertEqual(obj.last_name, kwargs["last_name"])

    def test_str(self):
        '''
        testing printing object in required format
        '''
        obj = User()
        expected = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected)

    def test_save(self):
        '''
        testing saving objects
        '''
        obj = User()
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
        obj = User()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "User")
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())
        self.assertNotIn("name", obj_dict)


if __name__ == '__main__':
    unittest.main()

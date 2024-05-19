#!/usr/bin/python3
'''
unittest module for Amenity class
'''
import unittest
from models.amenity import Amenity
from datetime import datetime
import uuid
from unittest.mock import patch


class TestAmenity(unittest.TestCase):
    '''
    Test cases for Amenity class methods and attributes
    '''

    def test_init_NoKwargs(self):
        '''
        Test initialization without kwargs
        '''
        with patch('models.storage.new') as mock_storage_new:
            obj = Amenity()
            self.assertIsInstance(obj, Amenity)
            self.assertTrue(hasattr(obj, "id"))
            self.assertTrue(hasattr(obj, "created_at"))
            self.assertTrue(hasattr(obj, "updated_at"))
            self.assertTrue(hasattr(obj, "name"))
            self.assertEqual(obj.name, "")
            self.assertEqual(obj.created_at, obj.updated_at)
            mock_storage_new.assert_called_once_with(obj)

    def test_init_kwargs(self):
        '''
        Test initialization with kwargs
        '''
        kwargs = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "name": "Pool"
        }
        obj = Amenity(**kwargs)
        self.assertEqual(obj.id, kwargs["id"])
        self.assertEqual(obj.created_at,
                         datetime.fromisoformat(kwargs["created_at"]))
        self.assertEqual(obj.updated_at,
                         datetime.fromisoformat(kwargs["updated_at"]))
        self.assertEqual(obj.name, kwargs["name"])

    def test_str(self):
        '''
        Test string representation
        '''
        obj = Amenity()
        expected = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected)

    def test_save(self):
        '''
        Test save method updates 'updated_at'
        '''
        obj = Amenity()
        old_updated_at = obj.updated_at
        with patch('models.storage.save') as mock_storage_save:
            obj.save()
            self.assertNotEqual(old_updated_at, obj.updated_at)
            self.assertTrue(obj.updated_at > old_updated_at)
            mock_storage_save.assert_called_once()

    def test_to_dict(self):
        '''
        Test to_dict method
        '''
        obj = Amenity()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "Amenity")
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())
        self.assertNotIn("name", obj_dict)


if __name__ == "__main__":
    unittest.main()

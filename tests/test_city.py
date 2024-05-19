#!/usr/bin/python3
"""
Unittest for City class
"""

import unittest
from models.city import City
from datetime import datetime
import uuid
from unittest.mock import patch


class TestCity(unittest.TestCase):
    """
    Test cases for City class
    """

    def test_init_no_kwargs(self):
        """
        Test initialization without kwargs
        """
        with patch('models.storage.new') as mock_storage_new:
            city = City()
            self.assertIsInstance(city, City)
            self.assertTrue(hasattr(city, "id"))
            self.assertTrue(hasattr(city, "created_at"))
            self.assertTrue(hasattr(city, "updated_at"))
            self.assertEqual(city.created_at, city.updated_at)
            self.assertEqual(city.state_id, "")
            self.assertEqual(city.name, "")
            mock_storage_new.assert_called_once_with(city)

    def test_init_with_kwargs(self):
        """
        Test initialization with kwargs
        """
        kwargs = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "state_id": "test_state_id",
            "name": "test_name"
        }
        city = City(**kwargs)
        self.assertEqual(city.id, kwargs["id"])
        self.assertEqual(city.created_at,
                         datetime.fromisoformat(kwargs["created_at"]))
        self.assertEqual(city.updated_at,
                         datetime.fromisoformat(kwargs["updated_at"]))
        self.assertEqual(city.state_id, kwargs["state_id"])
        self.assertEqual(city.name, kwargs["name"])

    def test_str(self):
        """
        Test string representation of City object
        """
        city = City()
        expected = f"[{city.__class__.__name__}] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected)

    def test_save(self):
        """
        Test save method for City object
        """
        city = City()
        old_updated_at = city.updated_at
        with patch('models.storage.save') as mock_storage_save:
            city.save()
            self.assertNotEqual(old_updated_at, city.updated_at)
            self.assertTrue(city.updated_at > old_updated_at)
            mock_storage_save.assert_called_once()

    def test_to_dict(self):
        """
        Test to_dict method for City object
        """
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["id"], city.id)
        self.assertEqual(city_dict["created_at"], city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], city.updated_at.isoformat())
        self.assertNotIn("name", city_dict)
        self.assertNotIn("state_id", city_dict)


if __name__ == "__main__":
    unittest.main()

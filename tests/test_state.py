#!/usr/bin/python3
"""
Unittest for State class
"""

import unittest
from models.state import State
from datetime import datetime
import uuid
from unittest.mock import patch


class TestState(unittest.TestCase):
    """
    Test cases for State class
    """

    def test_init_no_kwargs(self):
        """
        Test initialization without kwargs
        """
        with patch('models.storage.new') as mock_storage_new:
            state = State()
            self.assertIsInstance(state, State)
            self.assertTrue(hasattr(state, "id"))
            self.assertTrue(hasattr(state, "created_at"))
            self.assertTrue(hasattr(state, "updated_at"))
            self.assertEqual(state.created_at, state.updated_at)
            self.assertEqual(state.name, "")
            mock_storage_new.assert_called_once_with(state)

    def test_init_with_kwargs(self):
        """
        Test initialization with kwargs
        """
        kwargs = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "name": "California"
        }
        state = State(**kwargs)
        self.assertEqual(state.id, kwargs["id"])
        self.assertEqual(state.created_at,
                         datetime.fromisoformat(kwargs["created_at"]))
        self.assertEqual(state.updated_at,
                         datetime.fromisoformat(kwargs["updated_at"]))
        self.assertEqual(state.name, kwargs["name"])

    def test_str(self):
        """
        Test string representation of State object
        """
        state = State()
        class_name = state.__class__.__name__
        expected = f"[{class_name}] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), expected)

    def test_save(self):
        """
        Test save method for State object
        """
        state = State()
        old_updated_at = state.updated_at
        with patch('models.storage.save') as mock_storage_save:
            state.save()
            self.assertNotEqual(old_updated_at, state.updated_at)
            self.assertTrue(state.updated_at > old_updated_at)
            mock_storage_save.assert_called_once()

    def test_to_dict(self):
        """
        Test to_dict method for State object
        """
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["id"], state.id)
        self.assertEqual(state_dict["created_at"],
                         state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"],
                         state.updated_at.isoformat())
        self.assertNotIn("name", state_dict)


if __name__ == "__main__":
    unittest.main()

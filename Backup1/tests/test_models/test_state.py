#!/usr/bin/python3
"""Unit tests for the `State` module.

Test classes:
    TestStateInitialization - Test initialization of the State class.
    TestStateMethods - Test various methods of the State class.
"""
import unittest
import os
from models.state import State
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestStateInitialization(unittest.TestCase):
    """Test cases for initializing instances of the `State` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test initialization with parameters."""
        state1 = State()
        state3 = State("hello", "wait", "in")
        key = f"{type(state1).__name__}.{state1.id}"

        # Test class attributes
        self.assertIsInstance(state1.name, str)
        self.assertEqual(state3.name, "")
        state1.name = "Chicago"
        self.assertEqual(state1.name, "Chicago")
        self.assertIn(key, storage.all())

    def test_init(self):
        """Test public instance attributes."""
        state1 = State()
        state2 = State(**state1.to_dict())
        self.assertIsInstance(state1.id, str)
        self.assertIsInstance(state1.created_at, datetime)
        self.assertIsInstance(state1.updated_at, datetime)
        self.assertEqual(state1.updated_at, state2.updated_at)


class TestStateMethods(unittest.TestCase):
    """Test cases for various methods of the `State` class."""

    def test_str_representation(self):
        """Test string representation of a State instance."""
        state1 = State()
        string = f"[{type(state1).__name__}] ({state1.id}) {state1.__dict__}"
        self.assertEqual(state1.__str__(), string)

    def test_save_method(self):
        """Test the `save` method of the State class."""
        state1 = State()
        old_updated_at = state1.updated_at
        state1.save()
        self.assertNotEqual(state1.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test the `to_dict` method of the State class."""
        state1 = State()
        state2 = State(**state1.to_dict())
        state_dict = state2.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], type(state2).__name__)
        self.assertIn('created_at', state_dict.keys())
        self.assertIn('updated_at', state_dict.keys())
        self.assertNotEqual(state1, state2)


if __name__ == "__main__":
    unittest.main()

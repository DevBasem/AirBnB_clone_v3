#!/usr/bin/python3
"""Unit tests for the `Amenity` module.

Test classes:
    TestAmenityInitialization - Test initialization of the Amenity class.
    TestAmenityMethods - Test various methods of the Amenity class.
"""
import unittest
import os
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenityInitialization(unittest.TestCase):
    """Test cases for initializing instances of the `Amenity` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test initialization with parameters."""
        amenity1 = Amenity()
        amenity2 = Amenity(**amenity1.to_dict())
        amenity3 = Amenity("hello", "wait", "in")

        key = f"{type(amenity1).__name__}.{amenity1.id}"
        self.assertIsInstance(amenity1.name, str)
        self.assertIn(key, storage.all())
        self.assertEqual(amenity3.name, "")

    def test_init(self):
        """Test public instance attributes."""
        amenity1 = Amenity()
        amenity2 = Amenity(**amenity1.to_dict())
        self.assertIsInstance(amenity1.id, str)
        self.assertIsInstance(amenity1.created_at, datetime)
        self.assertIsInstance(amenity1.updated_at, datetime)
        self.assertEqual(amenity1.updated_at, amenity2.updated_at)


class TestAmenityMethods(unittest.TestCase):
    """Test cases for various methods of the `Amenity` class."""

    def test_str_representation(self):
        """Test string representation of an Amenity instance."""
        amenity = Amenity()
        string = f"[{type(amenity).__name__}] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(amenity.__str__(), string)

    def test_save_method(self):
        """Test the `save` method of the Amenity class."""
        amenity = Amenity()
        old_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test the `to_dict` method of the Amenity class."""
        amenity1 = Amenity()
        amenity2 = Amenity(**amenity1.to_dict())
        amenity_dict = amenity2.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], type(amenity2).__name__)
        self.assertIn('created_at', amenity_dict.keys())
        self.assertIn('updated_at', amenity_dict.keys())
        self.assertNotEqual(amenity1, amenity2)


if __name__ == "__main__":
    unittest.main()

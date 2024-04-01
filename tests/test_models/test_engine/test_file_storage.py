#!/usr/bin/python3
"""
Contains the TestFileStorageDocs and TestFileStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test tests/test_models/test_engine/test_file_storage.py
        conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class needs a docstring")

    def test_fs_func_docstrings(self):
        """Test for the presence of docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_get_method(self):
        """Test get method"""
        state = State(name="California")
        models.storage.new(state)
        models.storage.save()
        obj = models.storage.get(State, state.id)
        self.assertEqual(obj, state)

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_get_method_nonexistent_id(self):
        """Test get method with nonexistent ID"""
    obj = models.storage.get(State, "nonexistent_id")
    self.assertIsNone(obj)

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_count_method(self):
        """Test count method"""
    count = models.storage.count(State)
    self.assertEqual(count, 0)  # Replace 0 with the expected count
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "not testing file storage")
    def test_count(self):
        storage = FileStorage()
        length = len(storage.all())
        self.assertEqual(storage.count(), length)
        state_len = len(storage.all("State"))
        self.assertEqual(storage.count("State"), state_len)
        new = State()
        new.save()
        self.assertEqual(storage.count(), length + 1)
        self.assertEqual(storage.count("State"), state_len + 1)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Module containing the FileStorage class
"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}


class FileStorage:
    """
    FileStorage class for serializing instances to JSON file
    and deserializing JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of objects filtered by class type.

        Args:
            cls: The class type to filter by.

        Returns:
            dict: Dictionary of objects of the specified class type.
        """
        if cls:
            return {
                k: v
                for k, v in self.__objects.items()
                if isinstance(v, cls)
            }
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: Object to be set in __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists and is valid JSON)
        """
        try:
            with open(self.__file_path, 'r') as file:
                try:
                    loaded_objects = json.load(file)

                    for key, value in loaded_objects.items():
                        class_name, obj_id = key.split('.')
                        if 'created_at' in value and 'updated_at' in value:
                            value['created_at'] = datetime.strptime(
                                value['created_at'], "%Y-%m-%dT%H:%M:%S.%f"
                            )
                            value['updated_at'] = datetime.strptime(
                                value['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"
                            )

                            obj_class = classes.get(class_name)
                            if obj_class:
                                obj_instance = obj_class(**value)
                                self.__objects[key] = obj_instance
                except json.decoder.JSONDecodeError:
                    pass  # Invalid JSON in the file, ignore
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes the specified object from __objects.

        Args:
            obj: Object to be deleted.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """
        Calls the reload() method for deserializing the JSON file to objects.
        """
        self.reload()

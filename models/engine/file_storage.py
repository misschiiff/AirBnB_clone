#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        dict_key = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({dict_key: obj})

    def save(self):
        """ serializes __objects to the JSON file """
        dict = {}
        for key in self.__objects:
            dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                json_obj = json.load(f)
            for key, val in json_obj.items():
                self.__objects[key] = eval(val["__class__"])(**val)

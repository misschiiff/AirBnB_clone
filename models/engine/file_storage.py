#!/usr/bin/python3
""" File storage engine. """
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON filr to instances

    Private Class Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): empty but will store all objects by <class name>.id
    """
    __file_path = 'filestorage.json'
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[__class__.__name__].id

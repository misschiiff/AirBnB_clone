#!/usr/bin/python3
"""
Module base
"""
import json
import uuid
import datetime
# import csv
# import turtle
# import random


class BaseModel:
    """Base Model

    Represents a base class.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base method.

        Args:
            id (str): The unique id of the new BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return ('[{}] ({}) {}'.format(
            __class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute 'updated_at'. """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dictionary with all keys/values of __dict__ of the instance. """
        self.__dict__['__class__'] = __class__.__name__
        self.__dict__['created_at'] = str(self.created_at.isoformat())
        self.__dict__['updated_at'] = str(self.updated_at.isoformat())
        return (self.__dict__)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert python object to json string. """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save json string to file """
        with open(cls.__name__ + ".json", mode="w") as j_file:
            if list_objs is not None:
                list_dict = [item.to_dictionary() for item in list_objs]
                j_file.write(cls.to_json_string(list_dict))
            else:
                j_file.write(cls.to_json_string([]))

    @staticmethod
    def from_json_string(json_string):
        """ Convert json string to python object. """
        if json_string is None:
            return []
        return json.loads(json_string)

#!/usr/bin/python3
"""
Module base
"""
import json
import uuid
from datetime import datetime
import models
# import csv
# import turtle
# import random


class BaseModel:
    """
    Contains Class BaseModel

    Private Class Attributes:
        __time (str): time format.
    """
    global __time
    __time = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialize a new base method.

        Args:
            *args (ints): New attribute values.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                    kwargs["created_at"], __time).isoformat()
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], __time).isoformat()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # models.new(self)
            # models.save()

    def __str__(self):
        return ('[{}] ({}) {}'.format(
            __class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute 'updated_at'. """
        self.updated_at = datetime.now()
        # models.save()

    def to_dict(self):
        """ Returns a dictionary with all keys/values of __dict__ of the instance. """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(__time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(__time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

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

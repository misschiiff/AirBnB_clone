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
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     __time)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     __time)
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """ String representation """
        return ('[{:s}] ({:s}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute 'updated_at'. """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary with all keys/values of __dict__ of the instance.
        """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(__time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(__time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

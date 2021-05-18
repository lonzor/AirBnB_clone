#!/usr/bin/python3
"""
Module for BaseModel class
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Class that is the base of other models
    """

    def __init__(self):
        """
        Constructor of class BaseModel instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(tz=None)
        self.updated_at = self.created_at

    def __str__(self):
        """
        String representation of the instance created
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates 'updated_at' with current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """
        Returns dictionary containing all keys and values of instance
        Filters data that starts with underscores, methods, and functions.
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

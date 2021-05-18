#!/usr/bin/python3
"""
Module for BaseModel class
"""
import datetime
import uuid
import inspect


class BaseModel:
    """
    Class that is the base of other models
    """

    def __init__(self):
        """
        Constructor of class BaseModel instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of the instance created
        """
        return "[{}] ({}) {}".format(type(self), self.id, self.dict)

    def save(self):
        """
        Updates 'updated_at' with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns dictionary containing all keys and values of instance
        Filters data that starts with underscores, methods, and functions.
        """
        my_dict = {}
        my_dict['__class__'] = self.__name__
        self.created_at.isoformat()
        self.updated_at.isoformat()
        for i in inspect.getmembers(self):
            if not i[0].startswith("_"):
                if not inspect.ismethod(i[1] and not\
                       inspect.isfunction(i[1]):
                    my_dict[i[0]] = i[1]
        return my_dict

#!/usr/bin/python3
"""
This module contains the User class
"""
from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """Class for User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor of class User instance
        """
        if kwargs is not None and len(kwargs) != 0:
            for i in kwargs:
                if i == "__class__":
                    continue
                if i == "created_at" or i == "updated_at":
                    kwargs[i] = datetime.strptime(kwargs[i],
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, i, kwargs[i])
        else:
            super().__init__()

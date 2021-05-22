#!/usr/bin/python3
"""Module for class City. Inherits from BaseModel."""


from models.base_model import BaseModel


class City(BaseModel):
    """City data - state_id and name of city"""

    state_id = ""
    name = ""

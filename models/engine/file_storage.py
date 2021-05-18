#!/usr/bin/python3
"""
Module for class FileStorage
"""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file
    Deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the OBJ with key <obj class name>.id
        """
        new_obj = obj.to_dict()
        new_key = type(new_obj).__name__
        new_key += "." + obj.id
        self.__objects[new_key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file(path:__file_path)
        """
        dict2 = {}
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            for key, value in self.__objects.items():
                dict2[key] = value.to_dict()
            json.dump(dict2, f)
            """ json_str = json.dumps(self.__objects)
            f.write(json_str)
            """

    def reload(self):
        """
        Deserializes the JSON file to __objects
        Only if the JSON file __file_path exists
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                temp_objs = json.load(f)
                for k, v in temp_objs.items():
                    self.__objects[k] = BaseModel(**v)
                """self.__objects = json.loads(f.read())"""

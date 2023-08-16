#!/usr/bin/python3
"""module Filestorage that serialize and deserialize files"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        data = {}
        for k, v in self.__objects.items():
            data[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                data = f.read()
                data = json.loads(data)
                for k, v in data.items():
                    self.__objects[k] = classes[v["__class__"]](**v)
        except FileNotFoundError:
            pass

#!/usr/bin/python3
"""base Module"""
from ctypes import create_string_buffer
import json
from os import read


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer for Base class"""
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a
        list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a
        list of instances to a file
        """
        filename = cls.__name__ + ".json"
        dicList = []
        for obj in list_objs:
            dicList.append(obj.to_dictionary())

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
                return
            f.write(Base.to_json_string(dicList))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of the JSON string representation.
        """
        if json_string is None or (len(json_string) == 0):
            return([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already
        set.
        """
        dummy = cls(1, 1, 0)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a .json file"""
        dicList = []
        filename = cls.__name__ + ".json"
        with open(filename, mode='r', encoding='utf-8') as f:
            json_string = f.read()
            dicList = []
            for obj in cls.from_json_string(json_string):
                dicList.append(cls.create(**obj))
        return dicList

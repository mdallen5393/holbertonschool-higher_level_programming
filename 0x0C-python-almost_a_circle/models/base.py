#!/usr/bin/python3
"""base Module"""
import json


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
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        for dic in list_dictionaries:
            if type(dic) is not dict:
                err = "list_dictionaries must be a list of dictionaries"
                raise TypeError(err)
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a
        list of instances to a file
        """
        filename = cls.__name__ + ".json"
        dicList = []
        if list_objs is not None:
            for obj in list_objs:
                dicList.append(obj.to_dictionary())

        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dicList))

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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0, 0, 'a')
        if cls.__name__ == "Square":
            dummy = cls(1, 0, 0, 'b')
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a .json file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as f:
                json_string = f.read()
                dicList = []
                for obj in cls.from_json_string(json_string):
                    dicList.append(cls.create(**obj))
        except:
            dicList = []
        return dicList

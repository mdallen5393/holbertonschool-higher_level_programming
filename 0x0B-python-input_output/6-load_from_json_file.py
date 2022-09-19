#!/usr/bin/python3
"""6-load_from_json_file Module"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a "JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)

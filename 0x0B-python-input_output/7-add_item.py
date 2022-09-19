#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
then saves them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fname = "add_item.json"
ListyBoii = []

try:
    ListyBoii = load_from_json_file(fname)
except:
    pass

for i in range(1, len(sys.argv)):
    ListyBoii.append(sys.argv[i])
save_to_json_file(ListyBoii, fname)

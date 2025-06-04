#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """a function to serialize data to a json file"""
    with open(filename, "w") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """this loads the file content and deserialaizes it
    after doing it returns it"""
    with open(filename, "r") as f:
        return json.load(f)

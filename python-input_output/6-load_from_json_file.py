#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="UTF8") as f:
        return json.load(f)  # reads from a json 'txt' file and turn it into an object !.

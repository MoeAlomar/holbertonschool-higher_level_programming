#!/usr/bin/python3
"""
Module: 7-add_item.py

This module processes command line arguments and saves them to a JSON file.
It imports functions from external modules to handle JSON file operations.

Usage:
    python3 script_name.py [item1] [item2] [item3] ...

The script will save all command line arguments (except the script name)
to a file named 'add_item.json'.
"""

import sys
import os
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Create empty list to store command line arguments
filename = "add_item.json"
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Process command line arguments (skip script name at index 0)
for i in range(1, len(sys.argv)):
    items.append(sys.argv[i])

# Save the list to JSON file
save_to_json_file(items, "add_item.json")

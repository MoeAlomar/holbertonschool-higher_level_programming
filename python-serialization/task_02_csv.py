#!/usr/bin/python3
import csv
import json
def convert_csv_to_json(filename):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False

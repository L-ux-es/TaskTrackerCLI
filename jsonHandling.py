import json
import os.path

FILE_NAME = "tasks.json"


def write_json(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)


def read_json():
    if os.path.isfile(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
        return tasks
    return None

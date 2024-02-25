import json

def read_input(file_name):
  with open(file_name, "r") as json_file:
    json_object = json.load(json_file)
    return json_object

import json


class Deserialize:
    def __init__(self, path):
        self.path = path

    def single_employee_schema(self):
        with open(self.path, mode='r') as data_file:
            return json.load(data_file)

    def add_employee_schema(self):
        with open(self.path, mode='r') as data_file:
            return json.load(data_file)

    def all_employee_schema(self):
        with open(self.path, mode='r') as data_file:
            return json.load(data_file)

    def update_employee_schema(self):
        with open(self.path, mode='r') as data_file:
            return json.load(data_file)

    def part_update_employee_schema(self):
        with open(self.path, mode='r') as data_file:
            return json.load(data_file)

    def delete_employee_schema(self):
        with open(self.path, mode='r') as data_file:
            return json.load(data_file)



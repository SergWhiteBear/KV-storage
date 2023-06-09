import json


class KeyValueStorage:

    def __init__(self, storage_name):
        self.filename = storage_name
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def close(self):
        self.save_data()

    def __setitem__(self, key, value):
        self.data[key] = value
        self.save_data()

    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            raise KeyError(key)

    def __delitem__(self, key):
        try:
            del self.data[key]
            self.save_data()
        except KeyError:
            raise KeyError(key)

    def get_all_keys(self):
        return list(self.data.keys())

    def search_value(self, value):
        for key, val in self.data.items():
            if val == value:
                return key
        raise ValueError(value)

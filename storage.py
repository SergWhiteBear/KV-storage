import json
import os


class KeyValueStorage:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        try:
            with open(filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return str(self.data)

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def load(self):
        if not os.path.exists(f"{self.filename}.json"):
            self.save()
        with open(f"{self.filename}.json", "r") as f:
            self.data = json.load(f)

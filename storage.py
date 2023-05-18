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

    def save(self):
        with open(f"{self.filename}.json", 'w') as f:
            json.dump(self.data, f)

    def load(self):
        if not os.path.exists(f"{self.filename}.json"):
            self.save()
        with open(f"{self.filename}.json", "r") as f:
            self.data = json.load(f)

    @staticmethod
    def help():
        print("Available commands:")
        print("     1. add {key} {value} - adds a row key value to the storage")
        print("     2. get {key} - gets a value by the key")
        print("     3. del {key} - deletes a row key value to the storage")
        print("     4. all - shows all key values ")
        print("     5. len - count of key values")
        print("     6. save - saves added information")
        print("     7. exit - program exit")

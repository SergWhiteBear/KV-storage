from storage import KeyValueStorage


def interactive_mode(storage_name):
    storage = KeyValueStorage(storage_name)

    while True:
        command = input("Enter command:")
        if command == "add":
            args = input("Enter key and value:").split(" ")
            try:
                for i in range(0, len(args), 2):
                    key = args[i]
                    value = args[i + 1]
                    storage[key] = value
                    print(f"Set '{key}' to '{value}'.")
            except IndexError:
                print("Given 1 argument expect 2")
        elif command == "get":
            key = input("Enter key:")
            try:
                value = storage[key]
                print(f"{key} -> {value}")
            except KeyError:
                print(f"Key '{key}' not found.")
        elif command == "delete":
            key = input("Enter key:")
            try:
                del storage[key]
                print(f"Deleted '{key}'.")
            except KeyError:
                print(f"Key '{key}' not found.")
        elif command == "keys":
            print(f"Keys: {storage.get_all_keys()}")
        elif command == "search":
            value = input("Enter value:")
            try:
                key = storage.search_value(value)
                print(f"{value} -> {key}")
            except ValueError:
                print(f"Value '{value}' not found.")
        elif command == "show":
            for key in storage.get_all_keys():
                print(f"{key} -> {storage[key]}")
        elif command == "exit":
            storage.close()
            print("GoodBye!")
            break
        else:
            print("key-value storage\n"
                  "optional arguments:\n"
                  "get        get the value for the specified key\n"
                  "add      set the value for the specified key\n"
                  "delete     delete the specified key\n"
                  "keys                get all keys\n"
                  "search        value search\n"
                  "show                show all rows")

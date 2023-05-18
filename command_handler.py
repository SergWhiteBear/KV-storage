from storage import KeyValueStorage
from test_argparse import ArgParser
from simple_logwriter import LogWriter


def command_handler(input_data, storage):
    args = ArgParser.parse_args(input_data)
    LogWriter.write_log(LogWriter(), "log", args)
    command = args[0]
    if command == "add":
        key = args[1]
        value = args[2]
        try:
            storage[key] = value
            print(f"Pair {key}: {value} was added")
        except Exception as e:
            print(e)

    elif command == "get":
        key = args[1]
        try:
            print(storage[key])
        except Exception as e:
            print(e)

    elif command == "del":
        key = args[1]
        value = storage[key]
        try:
            del storage[key]
            print(f"{key}: {value} was deleted")
        except KeyError as e:
            print(e)

    elif command == "save":
        try:
            storage.save()
            print("Success save")
        except Exception as e:
            print(e)

    elif command == "all":
        print(f"{storage.data}")

    elif command == "len":
        print(len(storage))

    elif command == "help":
        storage.help()

    elif command == "exit":
        print("Good luck!")
        exit()

    else:
        print("Unknown command")


def run():
    filename = input("Put filename: ")
    storage = KeyValueStorage(filename)
    storage.load()
    while True:
        input_data = input("Put command: ")
        command_handler(input_data, storage)

import argparse
from storage import KeyValueStorage
from interactive_mode import interactive_mode


def main():
    parser = argparse.ArgumentParser(description='key-value storage')
    parser.add_argument(
        'filename',
        help='name of the storage file'
    )
    parser.add_argument(
        '--get',
        metavar='key',
        help='get the value for the specified key'
    )
    parser.add_argument(
        '--add',
        nargs='+',
        metavar=('key', 'value'),
        help='set the value for the specified key'
    )
    parser.add_argument(
        '--delete',
        metavar='key',
        help='delete the specified key'
    )
    parser.add_argument(
        '--keys',
        action='store_true',
        help='get all keys'
    )
    parser.add_argument(
        '--search',
        metavar='value',
        help='value search'
    )
    parser.add_argument(
        '--show',
        action='store_true',
        help='show all rows'
    )
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='interactive mode'
    )
    args = parser.parse_args()

    storage = KeyValueStorage(args.filename)

    if args.get:
        try:
            value = storage[args.get]
            print(value)
        except KeyError:
            print(f"Key '{args.get}' not found.")
    elif args.add:
        for i in range(0, len(args.add), 2):
            key = args.add[i]
            value = args.add[i + 1]
            storage[key] = value
            print(f"Set '{key}' to '{value}'.")
    elif args.delete:
        try:
            del storage[args.delete]
            print(f"Deleted '{args.delete}'.")
        except KeyError:
            print(f"Key '{args.delete}' not found.")
    elif args.keys:
        print(storage.get_all_keys())
    elif args.search:
        try:
            print(storage.search_value(args.search))
        except ValueError:
            print(f"Value '{args.search}' not found.")
    elif args.show:
        for key in storage.get_all_keys():
            print(f"{key} -> {storage[key]}")
    elif args.interactive:
        interactive_mode(args.filename)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

class ArgumentParser:

    @staticmethod
    def parse_args(input_data):
        first_arg = None
        second_arg = None
        args = input_data.split(' ')
        command = args[0]
        if len(args) == 2:
            first_arg = args[1]
        elif len(args) > 2:
            first_arg = args[1]
            second_arg = args[2]

        return command, first_arg, second_arg


argprs = ArgumentParser
print(argprs.parse_args("add key1 "))

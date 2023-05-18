from datetime import date, datetime


class LogWriter:

    def __init__(self):
        self.data = {}

    @staticmethod
    def get_time():
        t = datetime.now().strftime("%H:%M:%S")
        d = date.today()
        return f"{t} {d}"

    def write_log(self, filename, args):
        with open(f"{filename}.txt", "a") as f:
            f.write(f"{args[0]} {args[1]} {args[2]} {self.get_time()}\n")




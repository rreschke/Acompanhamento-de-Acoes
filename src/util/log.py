from datetime import datetime
from os import path
class Log:

    log: str = ""
    _root = path.dirname(path.abspath(__file__))

    @staticmethod
    def log_date_time(msg: str):
        Log.log += f"{datetime.now()} LOG: {msg}\n"

    @staticmethod
    def write_log():
        p = path.join(Log._root, f"../logs/{datetime.now().strftime('%H %M  %d%m%Y')}.txt")
        with open(p, "x") as f:
            f.write(Log.log)

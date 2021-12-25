from datetime import datetime
from os import path
class Log:

    log: str
    _root = path.dirname(path.abspath(__file__))

    @staticmethod
    def log_date_time(msg: str):
        print(f"{datetime.now()} LOG: {msg}")

    def write_log(self):
        with open(path.join(self._root, f"""src/logs/{datetime.now().strftime("%Y%m%d[%H:%M:%S")}.txt"""), "w") as f:
            f.write(self.log)

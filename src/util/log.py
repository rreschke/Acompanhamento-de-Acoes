from datetime import datetime

class Log:

    @staticmethod
    def log_date_time(msg: str):
        print(f"{datetime.now()} LOG: {msg}")
import sqlite3
from .enum import eQueryType
from .interface import iSQLite
from ...util.log import Log


class Repository(iSQLite):
    sqliteConnection: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self, db: str):
        Repository.sqliteConnection = sqlite3.connect(db)
        Repository.cursor = Repository.sqliteConnection.cursor()
        Log.log_date_time("Conectado ao banco SQLite.")

    @staticmethod
    def close_connection():
        Repository.cursor.close()
        Repository.sqliteConnection.close()

    @staticmethod
    def build_query(table: str, query_type: eQueryType, columns: list[str], values_list: list, filter: str = ""):
        if query_type == eQueryType.SEL:
            return f"""{query_type.value} {", ".join(columns)} FROM "{table}" {filter};"""

        elif query_type == eQueryType.INS:
            for i in range(len(values_list)):
                if type(values_list[i]) == str:
                    values_list[i] = f"\"{values_list[i]}\""
            return f"""{query_type.value} "{table}" ({", ".join(columns)}) values ({", ".join(values_list)});"""





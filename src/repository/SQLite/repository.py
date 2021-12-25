import sqlite3
from .enum import eQueryType
from .interface import iSQLite


class Repository(iSQLite):
    sqliteConnection: sqlite3.Connection
    cursor: sqlite3.Cursor

    @staticmethod
    def connect(db: str):
        sqlite_connection = sqlite3.connect(db)
        cursor = sqlite_connection.cursor()
        return sqlite_connection, cursor

    @staticmethod
    def build_query(table: str, query_type: eQueryType, columns: list[str], values_list: list, filter: str = ""):
        if query_type == eQueryType.SEL:
            return f"""{query_type.value} {", ".join(columns)} FROM "{table}" {filter};"""

        elif query_type == eQueryType.INS:
            for i in range(len(values_list)):
                if type(values_list[i]) == str:
                    values_list[i] = f"\"{values_list[i]}\""
            return f"""{query_type.value} "{table}" ({", ".join(columns)}) values ({", ".join(values_list)});"""





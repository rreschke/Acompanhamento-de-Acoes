import sqlite3


class RepositorySQL:
    sqliteConnection: sqlite3.Connection
    cursor: sqlite3.Cursor

    @staticmethod
    def connect(db: str):
        sqliteConnection = sqlite3.connect(db)
        cursor = sqliteConnection.cursor()
        return sqliteConnection, cursor

    @staticmethod
    def build_query(table: str, columns: list[str], column_types: list[]):

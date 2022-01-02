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
        Log.log_date_time("Encerrando cursor SQLite.")
        Repository.sqliteConnection.close()
        Log.log_date_time("Fechando conexão ao banco SQLite.")

    @staticmethod
    def build_query(table: str, query_type: eQueryType, columns: list[str], values_list: list, filter: str = ""):
        if query_type == eQueryType.SEL:
            return f"""{query_type.value} {", ".join(columns)} FROM "{table}" {filter};"""

        elif query_type == eQueryType.INS:
            for i in range(len(values_list)):
                if type(values_list[i]) == str:
                    values_list[i] = f"\"{values_list[i]}\""
            return f"""{query_type.value} "{table.replace(";", "").replace("-", "")}" 
                    ({", ".join(columns).replace(";", "").replace("-", "")}) values 
                    ({", ".join(values_list).replace(";", "").replace("-", "")});"""

        elif query_type == eQueryType.UPD:
            col_val = []
            for i in range(len(columns)):
                col_val.append(f"""{columns[i]} = {values_list[i]}""")
            return f"""{query_type.value} {table.replace(";", "").replace("-", "")} SET 
                        {", ".join(col_val).replace(";", "").replace("-", "")} 
                        {filter.replace(";", "").replace("-", "")};"""

        elif query_type == eQueryType.DEL:
            return f"""{query_type.value} FROM {table.replace(";", "").replace("-", "")} 
                        {filter.replace(";", "").replace("-", "")}"""

        else:
            return "Tipo de Query Não Implementado."

    def exec_query(query: str):
        try:
            Repository.cursor.execute(query)
        except():
            Log.log_date_time(f"Erro ao executar query \"{query}\"")
            Repository.sqliteConnection.rollback()
        finally:
            Repository.sqliteConnection.commit()






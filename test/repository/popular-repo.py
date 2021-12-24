import sqlite3
from src.source.requests.requests import Requests
import json
from src.repository.SQLite.repositorySQL import *

try:
    sqliteConnection, cursor = RepositorySQL.connect("repository-test.db")
    print("Database Successfully Connected to SQLite")

    con = Requests().get_json_api_b3(path="empresa")
    json = json.loads(con)

    for empresa in json:
        nm_tickers = empresa["cd_acao"]
        nm_empresa = empresa["nm_empresa"]
        nm_setor = empresa["setor_economico"]
        nm_subsetor = empresa["subsetor"]
        nm_segmento = empresa["segmento"]
        nr_cnpj = empresa["vl_cnpj"]

        nm_ticker = nm_tickers.split(", ")
        for ticker in nm_ticker:
            if ticker != "":
                query = f"insert into \"atv.cadastro_ativo\" " \
                        "(nm_ticker, nm_empresa, nm_setor, nm_subsetor, nm_segmento, nr_cnpj) " \
                        "values " \
                        f"(\"{ticker}\", \"{nm_empresa}\", \"{nm_setor}\", \"{nm_subsetor}\", \"{nm_segmento}\", {nr_cnpj});"
                cursor.execute(query)
                print("Query: ", query)

    sqliteConnection.commit()
    cursor.close()
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
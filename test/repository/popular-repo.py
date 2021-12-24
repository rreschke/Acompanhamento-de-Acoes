from src.source.requests.apib3.requests import *
import json
from src.repository.SQLite.repository import *

try:
    sqliteConnection, cursor = Repository.connect("repository-test.db")
    print("Database Successfully Connected to SQLite")

    con = Requests().get_json(path="empresa")
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
                query = Repository.build_query(table="atv.cadastro_ativo",
                                               query_type=eQueryType.INS,
                                               columns=["nm_ticker", "nm_empresa", "nm_setor",
                                                        "nm_subsetor", "nm_segmento", "nr_cnpj"],
                                               values_list=[ticker, nm_empresa, nm_setor, nm_subsetor, nm_segmento,
                                                            nr_cnpj])

                print("Query: ", query)
                cursor.execute(query)

    sqliteConnection.commit()
    cursor.close()
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
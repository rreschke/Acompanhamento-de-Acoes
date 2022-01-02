from src.repository.SQLite.repository import Repository
from src.repository.SQLite.enum.eQueryType import eQueryType
from src.util.log import Log

#Cria conexão
Repository("repository-test.db")


query_ins = Repository.build_query(table="atv.cadastro_ativo",
                                                   query_type=eQueryType.INS,
                                                   columns=["nm_ticker", "nm_empresa", "nm_setor",
                                                            "nm_subsetor", "nm_segmento", "nr_cnpj"],
                                                   values_list=["TESTE", "Empresa Teste", "Setor Teste", "Sub Setor Teste",
                                                                "Segmento teste", "1000222123422"])
query_select = Repository.build_query(table="atv.cadastro_ativo",
                                                   query_type=eQueryType.SEL,
                                                   columns=["nm_ticker", "nm_empresa", "nm_setor",
                                                            "nm_subsetor", "nm_segmento", "nr_cnpj"])

query_upd = Repository.build_query(table="atv.cadastro_ativo",
                                                   query_type=eQueryType.UPD,
                                                   columns=["nm_ticker", "nm_empresa", "nm_setor",
                                                            "nm_subsetor", "nm_segmento", "nr_cnpj"],
                                                   values_list=["TESTE2", "Empresa Teste2", "Setor Teste2", "Sub Setor Teste",
                                                                "Segmento teste", "1000222123422"],
                                                   filter = "WHERE nm_ticker = \"TESTE\"")

query_del = Repository.build_query(table="atv.cadastro_ativo",
                                                   query_type=eQueryType.DEL,
                                                   filter = "WHERE nm_ticker = \"TESTE2\"")

Repository.exec_query(query_ins)
Repository.exec_query(query_select)
Repository.exec_query(query_upd)
Repository.exec_query(query_del)
Log.write_log()





Repository.close_connection()

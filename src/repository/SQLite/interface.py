from abc import ABC, abstractmethod
from .enum import eQueryType
from ..interface import IRepositoryG


class iSQLite(IRepositoryG, ABC):
    """
        Interface para SQLite
    """

    @abstractmethod
    def close_connection(self):
        pass

    @abstractmethod
    def build_query(table: str, query_type: eQueryType, columns: list[str], values_list: list, filter: str = ""):
        """ Cria um query """
        pass
from abc import ABC, abstractmethod
from src.models.enum.eQueryType import eQueryType

class iSQLite(ABC):
    """
        Interface para SQLite
    """

    @abstractmethod
    def connect(db: str):
        """ Cria conexão com o db """
        pass

    @abstractmethod
    def build_query(table: str, query_type: eQueryType, columns: list[str], values_list: list, filter: str = ""):
        """ Cria um query """
        pass
from os import path
import json
from src.repository.interface import IRepositoryG
from src.repository.SQLite.repository import Repository as SQLite
from src.source.requests.interface import IRequestG
from src.util.log import Log


class Start:
    _root = path.dirname(path.abspath(__file__))
    _cfgpath = path.join(_root, "config/project.json")
    _repo: IRepositoryG
    _requests: IRequestG

    def __init__(self):
        config = json.load(open(self._cfgpath))
        repo = config["repository"]
        req = config["requests"]

        # conexao com o banco
        if repo == "SQLite":
            self._repo = SQLite(path.join(path.dirname(path.abspath(__file__)), "repository/SQLite/repository.db"))

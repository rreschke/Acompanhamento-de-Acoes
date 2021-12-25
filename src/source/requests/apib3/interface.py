from abc import ABC, abstractmethod
from ..interface import IRequestG


class IRequest(IRequestG, ABC):
    """ Interface de Request """

    @abstractmethod
    def get_json(self, path: str):
        pass
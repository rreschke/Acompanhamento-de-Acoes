from abc import ABC, abstractmethod
from ..interface import IRequestG


class IRequest(ABC, IRequestG):
    """ Interface de Request """

    @abstractmethod
    def get_html_papel_statusinvest(self, ticker: str):
        pass
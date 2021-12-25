from abc import ABC, abstractmethod
from ..interface import IRequestG


class IRequest(IRequestG, ABC):
    """ Interface de Request """

    @abstractmethod
    def get_html_papel_fundamentus(self, ticker: str):
        pass

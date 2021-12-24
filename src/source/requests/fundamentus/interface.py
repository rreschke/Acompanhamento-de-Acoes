from abc import ABC, abstractmethod


class IRequest(ABC):
    """ Interface de Request """

    @abstractmethod
    def get_content_by_url(self, url: str):
        pass

    @abstractmethod
    def get_html_papel_fundamentus(self, ticker: str):
        pass

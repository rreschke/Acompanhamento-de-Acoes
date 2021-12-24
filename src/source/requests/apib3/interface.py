from abc import ABC, abstractmethod


class IRequest(ABC):

    """ Interface de Request """

    @abstractmethod
    def get_content_by_url(self, url: str):
        pass

    @abstractmethod
    def get_json(self, path: str):
        pass
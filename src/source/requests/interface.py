from abc import ABC, abstractmethod


class IRequestG(ABC):
    """ Interface de Request """

    @abstractmethod
    def get_content_by_url(self, url: str):
        pass
import requests
import json
from pathlib import Path
from .interface import IRequest


class Requests(IRequest):
    config = json.load(open(Path(__file__).parent.parent.parent.joinpath('config/requests.json')))

    def get_content_by_url(self, url: str):
        r = requests.get(url)
        return r.content

    def get_json(self, path: str):
        url = self.config["apib3"] + path
        return self.get_content_by_url(url)

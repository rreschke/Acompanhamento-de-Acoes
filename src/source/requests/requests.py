import requests
import json
from pathlib import Path


class Requests:
    config = json.load(open(Path(__file__).parent.parent.parent.joinpath('config/requests.json')))

    def get_content_by_url(self, url: str):
        r = requests.get(url)
        return r.content

    def get_html_papel_statusinvest(self, ticker: str):
        url = self.config["url-papeis-statusinvest"] + ticker.lower()
        return self.get_content_by_url(url)

    def get_html_papel_fundamentus(self, ticker: str):
        url = self.config["url-papeis-fundamentus"] + ticker.upper()
        return self.get_content_by_url(url)

    def get_json_api_b3(self, path: str):
        url = self.config["api-b3"] + path
        return self.get_content_by_url(url)

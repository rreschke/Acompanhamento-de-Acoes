import requests
import json

class Requests:
    config = json.load(open('../../config/requests.json'))

    def getHTMLByURL(self, url: str):
        r = requests.get(url)
        return r.content

    def getHTMLPapelStatusInvest(self, ticker: str):
        url = self.config["url-papeis-statusinvest"] + ticker.lower()
        return self.getHTMLByURL(url)

    def getHTMLPapelFundamentus(self, ticker: str):
        url = self.config["url-papeis-fundamentus"] + ticker.upper()
        return self.getHTMLByURL(url)

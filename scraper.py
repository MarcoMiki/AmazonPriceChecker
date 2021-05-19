from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self, url):
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
        self.response = requests.get(url=url, headers=self.headers)
        self.data = self.response.text
        self.soup = BeautifulSoup(self.data, "html.parser")
        self.price = self.soup.find(id="price_inside_buybox").getText()

    def check_price(self, target_price):
        if float(self.price[2:]) <= float(target_price):
            return True

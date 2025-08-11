import requests
from bs4 import *


class Parser:

    @staticmethod
    def get_hrefs():
        url = "https://health-diet.ru/base_of_food/food_24526/?utm_source=leftMenu&utm_medium=base_of_food"
        hrefs = dict()

        headers = {
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
        }

        response = requests.get(url, headers=headers)

        scr = response.text
        soup = BeautifulSoup(scr, "lxml")
        products_table = soup.find(
            class_="uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed").find(
            "tbody").find_all(
            "tr")
        for product in products_table:
            product_head = product.find("a")
            title = product_head.get_text()
            href = product_head.get("href")
            hrefs[title] = href

        return hrefs

    @staticmethod
    def get_titles(hrefs: dict) -> list[str]:
        pass
from bs4 import BeautifulSoup
import requests
from constants import HEADERS


def scrape_item_price(url: str):
    page_content = _fetch_page(url)
    soup = BeautifulSoup(page_content, "lxml")
    price_text = soup.find("span", class_="a-offscreen").getText()
    price = float(price_text.split("zł")[0].replace(",", "."))
    return price


def _fetch_page(url: str):
    response = requests.get(url=url, headers=HEADERS)
    response.raise_for_status()
    return response.text

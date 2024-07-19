from scraper import scrape_item_price
from send_email import send_email
import json
import os

DIRNAME = os.path.dirname(__file__)
FILENAME = os.path.join(DIRNAME, "item.json")


def _load_item_data(filename: str):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data.get("url"), data.get("price")
    except FileNotFoundError as e:
        print(f"No such file: {filename}. {e}")
        return None, None
    except json.JSONDecodeError as e:
        print(f"Error with JSON file: {e}")
        return None, None


def main():
    url, target_price = _load_item_data(FILENAME)

    if not url or target_price is None:
        print("Invalid item data.")
        return

    current_price = scrape_item_price(url)

    if current_price is not None and current_price <= target_price:
        send_email(current_price, url)


if __name__ == "__main__":
    main()

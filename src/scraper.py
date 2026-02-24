import requests
import re
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def scrape_books(pages=2):
    books = []

    for page in range(1, pages + 1):
        url = BASE_URL.format(page)
        response = requests.get(url)
        response.encoding = "utf-8"  # força encoding correto

        soup = BeautifulSoup(response.text, "lxml")
        items = soup.select("article.product_pod")

        for item in items:
            title = item.h3.a["title"]

            # Corrige o problema do símbolo £
            price_text = item.select_one(".price_color").get_text(strip=True)
            price_clean = re.sub(r"[^0-9.]", "", price_text)
            price_gbp = float(price_clean)

            rating = item.select_one(".star-rating")["class"][1]

            books.append({
                "title": title,
                "price_gbp": price_gbp,
                "rating": rating
            })

    return books


def books_to_rows(books):
    for b in books:
        yield b
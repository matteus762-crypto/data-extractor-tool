import argparse
from datetime import datetime

from src.scraper import scrape_books, books_to_rows
from src.clean import clean_books_csv
from src.utils import ensure_dirs, write_csv


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pages", type=int, default=2)
    return parser.parse_args()


def main():
    args = parse_args()
    ensure_dirs()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    raw_path = f"data/raw/books_raw_{timestamp}.csv"
    clean_path = f"data/processed/books_clean_{timestamp}.csv"

    books = scrape_books(pages=args.pages)
    write_csv(raw_path, books_to_rows(books))

    df = clean_books_csv(raw_path, clean_path)

    print("✅ Done!")
    print(f"Rows: {len(df)}")


if __name__ == "__main__":
    main()
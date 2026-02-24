import os
import csv

def ensure_dirs():
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

def write_csv(path, rows):
    rows = list(rows)
    if not rows:
        return

    keys = rows[0].keys()
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
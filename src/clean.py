import pandas as pd

def clean_books_csv(input_path, output_path):
    df = pd.read_csv(input_path)

    df = df.drop_duplicates()
    df = df.sort_values(by="price_gbp", ascending=False)

    df.to_csv(output_path, index=False)
    return df
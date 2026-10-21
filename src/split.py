import pandas as pd
from sklearn.model_selection import train_test_split

def load_split(path="data/processed/clean.parquet", test_size=0.2):
    df = pd.read_parquet(path)
    X, y = df.drop(columns=["label"]), df["label"]
    return train_test_split(X, y, test_size=test_size,
                            stratify=y, random_state=42)

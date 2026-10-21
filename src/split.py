"""Fixed train/test split shared by all models."""
import pandas as pd
from sklearn.model_selection import train_test_split

from src.prepare_data import OUT

RANDOM_STATE = 42


def load_split(path=OUT, test_size=0.2):
    df = pd.read_parquet(path)
    X, y = df.drop(columns="label"), df["label"]
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=RANDOM_STATE)

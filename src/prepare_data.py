"""Raw PhiUSIIL CSV -> data/processed/clean.parquet."""
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "PhiUSIIL_Phishing_URL_Dataset.csv"
OUT = ROOT / "data" / "processed" / "clean.parquet"

# free-text identifiers; the numeric features are derived from these
TEXT_COLS = ["FILENAME", "URL", "Domain", "TLD", "Title"]


def prepare(raw_path: Path = RAW, out_path: Path = OUT) -> pd.DataFrame:
    df = pd.read_csv(raw_path)
    df = df.drop_duplicates().dropna()
    df = df.drop(columns=[c for c in TEXT_COLS if c in df.columns])
    df["label"] = df["label"].astype(int)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out_path, index=False)
    return df


if __name__ == "__main__":
    if not RAW.exists():
        sys.exit(f"Missing {RAW}. Download the PhiUSIIL CSV first (see README).")
    df = prepare()
    print(f"Wrote {OUT} {df.shape}")
    print(df["label"].value_counts())

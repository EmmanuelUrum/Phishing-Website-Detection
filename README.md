# Phishing Website Detection

Classifying URLs as phishing or legitimate using the PhiUSIIL Phishing URL dataset.

## Team
- Juno: data preparation, EDA, preprocessing
- Emmanuel: train/test split, baseline and final models, evaluation

## Data
Download the PhiUSIIL Phishing URL dataset (UCI ML Repository) and place the CSV at
`data/raw/PhiUSIIL_Phishing_URL_Dataset.csv`. Raw data is not committed.

## How to run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m src.prepare_data      # raw CSV -> data/processed/clean.parquet
```
Then run the notebooks in `notebooks/` in order (01 to 04).

## Layout
- `data/` raw and processed data
- `notebooks/` EDA, preprocessing, baseline, models
- `src/` shared code (`prepare_data.py`, `split.py`, `evaluate.py`)
- `figures/` saved plots
- `reports/` metrics table and written reports

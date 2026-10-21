# Phishing Website Detection

Classifying URLs as phishing or legitimate using the PhiUSIIL Phishing URL dataset.

## Team
- Juno: data preparation, EDA, preprocessing
- Emmanuel: train/test split, baseline and final models, evaluation

## Setup after cloning

Run all commands from the repo root. You need Python 3.10 or newer.

### 1. Clone the repo
```bash
git clone https://github.com/EmmanuelUrum/Phishing-Website-Detection.git
cd Phishing-Website-Detection
```

### 2. Create a virtual environment and install packages
Linux / macOS:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Your prompt should now start with `(.venv)`. Re-activate it every time you open a new terminal.

### 3. Turn on notebook output stripping (once per clone)
```bash
nbstripout --install
```
This keeps notebook outputs out of your commits. Without it, notebooks create huge diffs and merge conflicts.

### 4. Get the data
1. Download the PhiUSIIL Phishing URL dataset from the UCI ML Repository.
2. Put the CSV here: `data/raw/PhiUSIIL_Phishing_URL_Dataset.csv`

Raw data is not committed to git.

### 5. Build the clean dataset
```bash
python -m src.prepare_data
```
This writes `data/processed/clean.parquet`. If that file is already in the repo, you can skip steps 4 and 5.

### 6. Open the notebooks
```bash
jupyter notebook
```
Open the files in `notebooks/` in order, 01 to 04.

## Using the shared code (for models)
```python
from src.split import load_split
from src.evaluate import evaluate

X_train, X_test, y_train, y_test = load_split()   # same split for everyone (random_state=42)
# ... train a model ...
metrics = evaluate(model, X_test, y_test, name="random_forest")
```
`load_split()` reads `data/processed/clean.parquet` relative to the current folder. Run Python from the repo root, or inside a notebook pass `load_split("../data/processed/clean.parquet")`.

Add each model's metrics to `reports/model_comparison.csv`.

## Troubleshooting
- `ModuleNotFoundError: No module named 'src'`: run from the repo root and use `python -m src.prepare_data`, not `python src/prepare_data.py`.
- `Missing .../PhiUSIIL_Phishing_URL_Dataset.csv`: the CSV is not in `data/raw/` or has a different name.
- `nbstripout: command not found`: activate the virtual environment first (step 2).

## Project layout
- `data/raw/` raw CSV (not committed)
- `data/processed/` cleaned dataset (`clean.parquet`)
- `notebooks/` 01 EDA, 02 preprocessing, 03 baseline, 04 models
- `src/` shared code: `prepare_data.py`, `split.py`, `evaluate.py`
- `figures/` saved plots
- `reports/` metrics table and written reports

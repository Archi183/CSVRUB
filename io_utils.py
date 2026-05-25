import pandas as pd
from pathlib import Path

def read_csv_smart(input_csv):
    try:
        return pd.read_csv(input_csv, dtype=str, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(input_csv, dtype=str, encoding="latin-1")

def ensure_out_dir(out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True)
    return out_dir

def write_csv(df, path):
    df.to_csv(path, index=False)
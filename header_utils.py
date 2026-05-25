import re

def normalize_header(col: str) -> str:
    col = str(col).strip()
    col = col.replace("\ufeff", "")  # BOM
    col = re.sub(r"\s+", "", col)
    return col

def normalize_headers(df):
    df = df.copy()
    df.columns = [normalize_header(c) for c in df.columns]
    return df
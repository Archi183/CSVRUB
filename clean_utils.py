import pandas as pd
import re

def clean_text(x):
    if pd.isna(x):
        return ""
    x = str(x)
    x = x.replace("\u00a0", " ")  # non-breaking space
    x = x.strip()
    x = re.sub(r"\s+", " ", x)
    return x

def normalize_email(x):
    x = clean_text(x)
    return x.lower()

def normalize_phone(x):
    x = clean_text(x)
    digits = re.sub(r"\D+", "", x)
    return digits

def clean_all_cells(df):
    return df.applymap(clean_text)
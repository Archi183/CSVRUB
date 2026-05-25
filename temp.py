import pandas as pd
import re
import sys
from pathlib import Path

def normalize_header(col: str) -> str:
    col = str(col).strip()
    col = col.replace("\ufeff", "")  # BOM
    col = re.sub(r"\s+", "_", col)
    return col

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
    # keep conservative; don't destroy numbers
    # if len(digits) == 12 and digits.startswith("91"):
    #     digits = digits[2:]
    return digits

def main(input_csv, out_dir="output"):
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True)

    # Try UTF-8 first, fallback to latin-1
    try:
        df = pd.read_csv(input_csv, dtype=str, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(input_csv, dtype=str, encoding="latin-1")

    # Normalize headers
    df.columns = [normalize_header(c) for c in df.columns]

    # Clean all text cells
    df = df.applymap(clean_text)

    # Normalize common columns if present
    for col in df.columns:
        cl = col.lower()
        if "email" in cl:
            df[col] = df[col].apply(normalize_email)
        if "phone" in cl:
            df[col] = df[col].apply(normalize_phone)

    # Choose dedupe key
    if "License_No" in df.columns:
        key = ["License_No"]
    elif "Email" in df.columns:
        key = ["Email"]
    elif "Business_Phone" in df.columns:
        key = ["Business_Phone"]
    else:
        key = df.columns.tolist()  # last resort: full row

    # Separate duplicates
    dup_mask = df.duplicated(subset=key, keep="first")
    duplicates = df[dup_mask].copy()
    cleaned = df[~dup_mask].copy()

    # Save outputs
    cleaned.to_csv(out_dir / "cleaned.csv", index=False)
    duplicates.to_csv(out_dir / "duplicates.csv", index=False)

    print("Done.")
    print(f"Rows in input: {len(df)}")
    print(f"Rows in cleaned: {len(cleaned)}")
    print(f"Duplicates removed: {len(duplicates)}")
    print(f"Saved: {out_dir/'cleaned.csv'}")
    print(f"Saved: {out_dir/'duplicates.csv'}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_crm_csv.py input.csv [output_dir]")
        sys.exit(1)

    input_csv = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) >= 3 else "output"
    main(input_csv, out_dir)
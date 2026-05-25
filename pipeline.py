from header_utils import normalize_headers
from clean_utils import clean_all_cells, normalize_email, normalize_phone
from io_utils import read_csv_smart, ensure_out_dir, write_csv
from dedupe_utils import choose_dedupe_key, split_duplicates
from report_utils import print_report

def run_pipeline(input_csv, out_dir, config):
    out_dir = ensure_out_dir(out_dir)

    df = read_csv_smart(input_csv)

    df = normalize_headers(df)
    df = clean_all_cells(df)

    # Normalize selected columns from config
    for col in config.get("email_cols", []):
        if col in df.columns:
            df[col] = df[col].apply(normalize_email)

    for col in config.get("phone_cols", []):
        if col in df.columns:
            df[col] = df[col].apply(normalize_phone)

    # Dedupe
    priority = config.get("dedupe_priority", [])
    key = choose_dedupe_key(df, priority)
    cleaned, duplicates = split_duplicates(df, key)

    # Save
    write_csv(cleaned, out_dir / "cleaned.csv")
    write_csv(duplicates, out_dir / "duplicates.csv")

    print_report(df, cleaned, duplicates, out_dir)
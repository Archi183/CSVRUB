def print_report(df, cleaned, duplicates, out_dir):
    print("Done.")
    print(f"Rows in input: {len(df)}")
    print(f"Rows in cleaned: {len(cleaned)}")
    print(f"Duplicates removed: {len(duplicates)}")
    print(f"Saved: {out_dir/'cleaned.csv'}")
    print(f"Saved: {out_dir/'duplicates.csv'}")
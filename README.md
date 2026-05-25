# CSVRUB

A configurable CSV cleaning pipeline built with Python and Pandas.

## What it does
- Auto-detects and normalizes messy headers
- Cleans whitespace, casing, and formatting across all cells
- Normalizes email addresses and phone numbers
- Detects and separates duplicate rows into a separate file
- Outputs a clean CSV + a duplicates CSV + a report

## Usage
```bash
python run.py configs/my_config.py input.csv output_dir
```

## Config
Create a config file (see `configs/` for example) to specify:
- Which columns contain emails or phone numbers
- Deduplication priority columns

## Output
- `output/cleaned.csv` — deduplicated, cleaned data
- `output/duplicates.csv` — flagged duplicate rows
- A printed report summarizing changes

## Built With
- Python
- Pandas

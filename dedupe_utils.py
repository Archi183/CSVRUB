def choose_dedupe_key(df, priority):
    """
    priority: list like ["License_No", "Email", "Business_Phone"]
    Returns: list[str] subset key or None
    """
    for col in priority:
        if col in df.columns:
            return [col]
    return None

def split_duplicates(df, key, keep="first"):
    """
    Returns: cleaned_df, duplicates_df
    """
    if not key:
        return df.copy(), df.iloc[0:0].copy()

    dup_mask = df.duplicated(subset=key, keep=keep)
    duplicates = df[dup_mask].copy()
    cleaned = df[~dup_mask].copy()
    return cleaned, duplicates
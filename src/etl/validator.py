def check_duplicates(df):
    """
    Returns number of duplicate rows
    """
    return df.duplicated().sum()


def check_missing_values(df):
    """
    Returns missing values per column
    """
    return df.isnull().sum()
import pandas as pd


def check_duplicates(df):
    return df.duplicated().sum()


def check_primary_key(df, column):
    return df[column].duplicated().sum()


def check_nulls(df):
    return df.isnull().sum().sum()


def check_positive_values(df, column):
    return (df[column] <= 0).sum()


def check_foreign_key(child_df, parent_df, child_col, parent_col):
    return (~child_df[child_col].isin(parent_df[parent_col])).sum()


def check_range(df, column, min_value, max_value):
    return ((df[column] < min_value) | (df[column] > max_value)).sum()

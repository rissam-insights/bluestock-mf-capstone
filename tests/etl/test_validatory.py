import pandas as pd

from src.etl.validator import (
    check_duplicates,
    check_primary_key,
    check_nulls,
    check_positive_values,
    check_range,
)


def test_check_duplicates():
    df = pd.DataFrame({"A": [1, 1, 2]})
    assert check_duplicates(df) == 1


def test_primary_key_unique():
    df = pd.DataFrame({"id": [1, 2, 3]})
    assert check_primary_key(df, "id") == 0


def test_null_values():
    df = pd.DataFrame({"A": [1, None, 3]})
    assert check_nulls(df) == 1


def test_positive_values():
    df = pd.DataFrame({"sales": [100, 200, -50]})
    assert check_positive_values(df, "sales") == 1


def test_range_check():
    df = pd.DataFrame({"score": [10, 20, 150]})
    assert check_range(df, "score", 0, 100) == 1
    
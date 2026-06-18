from src.etl.validator import check_duplicates


def test_check_duplicates_exists():
    assert callable(check_duplicates)


def test_validator_name():
    assert check_duplicates.__name__ == "check_duplicates"
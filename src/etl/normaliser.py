import re

def normalize_year(year):
    if year is None:
        return None

    year = str(year).strip()

    match = re.search(r'(\d{4})', year)

    if match:
        return int(match.group(1))

    return None


def normalize_ticker(ticker):
    if ticker is None:
        return None

    return str(ticker).strip().upper()
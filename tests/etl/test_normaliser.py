from src.etl.normaliser import normalize_year, normalize_ticker


def test_normalize_year_mar():
    assert normalize_year("Mar 2024") == 2024


def test_normalize_year_dec():
    assert normalize_year("Dec 2019") == 2019


def test_normalize_year_integer():
    assert normalize_year(2023) == 2023


def test_normalize_year_none():
    assert normalize_year(None) is None
    
    
    def test_normalize_ticker_spaces():
        assert normalize_ticker(" adanient ") == "ADANIENT"


def test_normalize_ticker_lowercase():
    assert normalize_ticker("tcs") == "TCS"


def test_normalize_ticker_mixed():
    assert normalize_ticker("ReLiAnCe") == "RELIANCE"


def test_normalize_ticker_none():
    assert normalize_ticker(None) is None
   
    def test_normalize_year_string():
        assert normalize_year("2025") == 2025


def test_normalize_year_with_text():
    assert normalize_year("FY 2022") == 2022


def test_normalize_year_empty():
    assert normalize_year("") is None


def test_normalize_year_invalid():
    assert normalize_year("ABC") is None
    
    def test_year_2019():
        assert normalize_year("Mar 2019") == 2019

def test_year_2020():
    assert normalize_year("Mar 2020") == 2020

def test_year_2021():
    assert normalize_year("Mar 2021") == 2021

def test_year_2022():
    assert normalize_year("Mar 2022") == 2022

def test_year_2023():
    assert normalize_year("Mar 2023") == 2023

def test_year_2024():
    assert normalize_year("Mar 2024") == 2024

def test_year_string():
    assert normalize_year("2018") == 2018

def test_year_float():
    assert normalize_year(2021.0) == 2021

def test_year_invalid():
    assert normalize_year("hello") is None

def test_year_empty():
    assert normalize_year("") is None
    def test_ticker_abb():
        assert normalize_ticker("abb") == "ABB"

def test_ticker_tcs():
    assert normalize_ticker("tcs") == "TCS"

def test_ticker_hdfc():
    assert normalize_ticker("hdfc") == "HDFC"

def test_ticker_icici():
    assert normalize_ticker("icici") == "ICICI"

def test_ticker_trim():
    assert normalize_ticker("  reliance  ") == "RELIANCE"

def test_ticker_upper():
    assert normalize_ticker("INFY") == "INFY"

def test_ticker_number():
    assert normalize_ticker("123") == "123"

def test_ticker_blank():
    assert normalize_ticker("") == ""

def test_ticker_space():
    assert normalize_ticker(" ") == ""

def test_ticker_special():
    assert normalize_ticker("adani-ent") == "ADANI-ENT"
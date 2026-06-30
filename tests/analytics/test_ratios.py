from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    roe,
    roce,
    roa,
    opm_cross_check,
    debt_to_equity,
    high_leverage_flag,
    interest_coverage_ratio,
    icr_label,
    icr_warning,
    net_debt,
    asset_turnover,
)


def test_net_profit_margin():
    assert net_profit_margin(100, 1000) == 10


def test_net_profit_margin_zero_sales():
    assert net_profit_margin(100, 0) is None


def test_operating_profit_margin():
    assert operating_profit_margin(200, 1000) == 20


def test_roe():
    assert roe(100, 200, 300) == 20


def test_roe_negative_equity():
    assert roe(100, -200, 100) is None


def test_roce():
    assert roce(100, 200, 300, 500) == 10


def test_roa():
    assert roa(100, 1000) == 10


def test_opm_cross_check():
    assert opm_cross_check(20, 18) is True


# ----------------------------
# Day 09 Tests
# ----------------------------

def test_debt_to_equity():
    assert debt_to_equity(500, 200, 300) == 1


def test_debt_free():
    assert debt_to_equity(0, 200, 300) == 0


def test_negative_equity_de():
    assert debt_to_equity(100, -200, 100) is None


def test_high_leverage_flag():
    assert high_leverage_flag(6, "Technology") is True


def test_interest_coverage():
    assert interest_coverage_ratio(100, 20, 10) == 12


def test_interest_zero():
    assert interest_coverage_ratio(100, 20, 0) is None


def test_icr_label():
    assert icr_label(None) == "Debt Free"


def test_icr_warning():
    assert icr_warning(1.2) is True


def test_net_debt():
    assert net_debt(500, 200) == 300


def test_asset_turnover():
    assert asset_turnover(1000, 500) == 2
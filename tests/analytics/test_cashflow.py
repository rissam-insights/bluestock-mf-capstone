from src.analytics.cashflow import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion,
    capital_allocation_pattern,
)


def test_free_cash_flow():
    assert free_cash_flow(500, -200) == 300


def test_cfo_quality_high():
    assert cfo_quality_score(200, 100) == "High Quality"


def test_cfo_quality_moderate():
    assert cfo_quality_score(75, 100) == "Moderate"


def test_cfo_quality_risk():
    assert cfo_quality_score(20, 100) == "Accrual Risk"


def test_cfo_quality_none():
    assert cfo_quality_score(100, 0) is None


def test_capex_asset_light():
    assert capex_intensity(-20, 1000) == "Asset Light"


def test_capex_moderate():
    assert capex_intensity(-50, 1000) == "Moderate"


def test_capex_capital_intensive():
    assert capex_intensity(-150, 1000) == "Capital Intensive"


def test_fcf_conversion():
    assert fcf_conversion(300, 600) == 50


def test_fcf_conversion_none():
    assert fcf_conversion(100, 0) is None


def test_reinvestor():
    assert capital_allocation_pattern(100, -50, -20) == "Reinvestor"


def test_shareholder_returns():
    assert capital_allocation_pattern(
        100, -50, -20, "High Quality"
    ) == "Shareholder Returns"


def test_liquidating_assets():
    assert capital_allocation_pattern(100, 50, -20) == "Liquidating Assets"


def test_distress_signal():
    assert capital_allocation_pattern(-100, 50, 20) == "Distress Signal"


def test_growth_funded():
    assert capital_allocation_pattern(-100, -50, 20) == "Growth Funded by Debt"


def test_cash_accumulator():
    assert capital_allocation_pattern(100, 50, 20) == "Cash Accumulator"


def test_pre_revenue():
    assert capital_allocation_pattern(-100, -50, -20) == "Pre-Revenue"


def test_mixed():
    assert capital_allocation_pattern(100, -50, 20) == "Mixed"
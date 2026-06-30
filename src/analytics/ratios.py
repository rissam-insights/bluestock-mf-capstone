def net_profit_margin(net_profit, sales):
    """
    Net Profit Margin = (Net Profit / Sales) * 100
    Return None if sales is 0.
    """
    if sales == 0:
        return None
    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    """
    Operating Profit Margin = (Operating Profit / Sales) * 100
    Return None if sales is 0.
    """
    if sales == 0:
        return None
    return (operating_profit / sales) * 100


def roe(net_profit, equity_capital, reserves):
    """
    Return on Equity = Net Profit / (Equity + Reserves) * 100
    Return None if Equity + Reserves <= 0.
    """
    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return (net_profit / equity) * 100


def roce(ebit, equity_capital, reserves, borrowings):
    """
    Return on Capital Employed
    ROCE = EBIT / (Equity + Reserves + Borrowings) * 100
    """
    capital_employed = equity_capital + reserves + borrowings

    if capital_employed <= 0:
        return None

    return (ebit / capital_employed) * 100


def roa(net_profit, total_assets):
    """
    Return on Assets
    ROA = Net Profit / Total Assets * 100
    """
    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100


def opm_cross_check(calculated_opm, reported_opm):
    """
    Returns True if difference is greater than 1%.
    """
    return abs(calculated_opm - reported_opm) > 1
def debt_to_equity(borrowings, equity_capital, reserves):
    """
    Debt-to-Equity Ratio
    Return 0 if borrowings are zero.
    Return None if equity is zero or negative.
    """
    equity = equity_capital + reserves

    if borrowings == 0:
        return 0

    if equity <= 0:
        return None

    return borrowings / equity


def high_leverage_flag(de_ratio, sector):
    """
    High leverage flag.
    """
    if sector == "Financials":
        return False

    return de_ratio is not None and de_ratio > 5


def interest_coverage_ratio(operating_profit, other_income, interest):
    """
    Interest Coverage Ratio.
    """
    if interest == 0:
        return None

    return (operating_profit + other_income) / interest


def icr_label(icr):
    """
    Label debt-free companies.
    """
    if icr is None:
        return "Debt Free"

    return ""


def icr_warning(icr):
    """
    Warning if ICR is below 1.5.
    """
    if icr is None:
        return False

    return icr < 1.5


def net_debt(borrowings, investments):
    """
    Net Debt.
    """
    return borrowings - investments


def asset_turnover(sales, total_assets):
    """
    Asset Turnover Ratio.
    """
    if total_assets == 0:
        return None

    return sales / total_assets
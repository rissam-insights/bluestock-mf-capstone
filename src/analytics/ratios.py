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
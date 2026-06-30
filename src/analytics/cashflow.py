def free_cash_flow(operating_activity, investing_activity):
    """
    Free Cash Flow
    FCF = CFO + Investing Activity

    Investing activity is usually negative,
    so simply add both values.
    """
    return operating_activity + investing_activity


def cfo_quality_score(cfo, pat):
    """
    CFO / PAT Quality Score

    >1.0 = High Quality
    0.5–1.0 = Moderate
    <0.5 = Accrual Risk
    """

    if pat == 0:
        return None

    ratio = cfo / pat

    if ratio > 1:
        return "High Quality"

    elif ratio >= 0.5:
        return "Moderate"

    return "Accrual Risk"


def capex_intensity(investing_activity, sales):
    """
    CapEx Intensity

    abs(CFI) / Sales ×100
    """

    if sales == 0:
        return None

    intensity = abs(investing_activity) / sales * 100

    if intensity < 3:
        return "Asset Light"

    elif intensity <= 8:
        return "Moderate"

    return "Capital Intensive"


def fcf_conversion(fcf, operating_profit):
    """
    FCF Conversion
    """

    if operating_profit == 0:
        return None

    return (fcf / operating_profit) * 100

def capital_allocation_pattern(cfo, cfi, cff, cfo_quality="Moderate"):
    """
    Capital Allocation Pattern Classifier

    Returns one of:
    Reinvestor
    Shareholder Returns
    Liquidating Assets
    Distress Signal
    Growth Funded by Debt
    Cash Accumulator
    Pre-Revenue
    Mixed
    """

    cfo_sign = "+" if cfo >= 0 else "-"
    cfi_sign = "+" if cfi >= 0 else "-"
    cff_sign = "+" if cff >= 0 else "-"

    pattern = (cfo_sign, cfi_sign, cff_sign)

    if pattern == ("+", "-", "-"):
        if cfo_quality == "High Quality":
            return "Shareholder Returns"
        return "Reinvestor"

    elif pattern == ("+", "+", "-"):
        return "Liquidating Assets"

    elif pattern == ("-", "+", "+"):
        return "Distress Signal"

    elif pattern == ("-", "-", "+"):
        return "Growth Funded by Debt"

    elif pattern == ("+", "+", "+"):
        return "Cash Accumulator"

    elif pattern == ("-", "-", "-"):
        return "Pre-Revenue"

    elif pattern == ("+", "-", "+"):
        return "Mixed"

    return "Unknown"
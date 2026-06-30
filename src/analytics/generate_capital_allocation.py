import pandas as pd
from pathlib import Path
from src.analytics.cashflow import (
    cfo_quality_score,
    capital_allocation_pattern,
)

BASE_DIR = Path(__file__).resolve().parents[2]

cashflow_path = BASE_DIR / "data" / "processed" / "cashflow.csv"
output_path = BASE_DIR / "output" / "capital_allocation.csv"

df = pd.read_csv(cashflow_path)

results = []

for _, row in df.iterrows():

    cfo = row.get("operating_activity", 0)
    cfi = row.get("investing_activity", 0)
    cff = row.get("financing_activity", 0)
    pat = row.get("net_profit", 0)

    quality = cfo_quality_score(cfo, pat)
    if quality is None:
        quality = "Moderate"

    pattern = capital_allocation_pattern(
        cfo,
        cfi,
        cff,
        quality,
    )

    results.append({
        "company_id": row.get("company_id"),
        "year": row.get("year"),
        "cfo_sign": "+" if cfo >= 0 else "-",
        "cfi_sign": "+" if cfi >= 0 else "-",
        "cff_sign": "+" if cff >= 0 else "-",
        "pattern_label": pattern,
    })

result_df = pd.DataFrame(results)

output_path.parent.mkdir(exist_ok=True)

result_df.to_csv(output_path, index=False)

print("✅ capital_allocation.csv created successfully")
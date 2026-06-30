import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

# Read required tables
companies = pd.read_sql("SELECT * FROM companies", conn)
financial_ratios = pd.read_sql("SELECT * FROM financial_ratios", conn)

print("Companies :", len(companies))
print("Financial Ratio Rows :", len(financial_ratios))

# Example computed column

if "Net Profit Margin %" not in financial_ratios.columns:
    financial_ratios["Net Profit Margin %"] = None

financial_ratios.to_sql(
    "financial_ratios",
    conn,
    if_exists="replace",
    index=False
)

print("\nFinancial Ratios table updated successfully.")

conn.close()
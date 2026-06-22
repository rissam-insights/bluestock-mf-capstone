import pandas as pd
import sqlite3

conn = sqlite3.connect("nifty100.db")

files = {
    "companies": "data/raw/companies.xlsx",
    "profitandloss": "data/raw/profitandloss.xlsx",
    "balancesheet": "data/raw/balancesheet.xlsx",
    "cashflow": "data/raw/cashflow.xlsx",
    "analysis": "data/raw/analysis.xlsx",
    "documents": "data/raw/documents.xlsx",
    "prosandcons": "data/raw/prosandcons.xlsx",
    "sectors": "data/raw/sectors.xlsx",
    "stock_prices": "data/raw/stock_prices.xlsx",
    "financial_ratios": "data/raw/financial_ratios.xlsx",
    "peer_groups": "data/raw/peer_groups.xlsx"
}

for table, file in files.items():
    try:
        df = pd.read_excel(file)

        # companies file fix
        if table == "companies":
            df.columns = df.iloc[1]
            df = df[2:].reset_index(drop=True)

        df.to_sql(
            table,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"✅ {table} loaded")

    except Exception as e:
        print(f"❌ {table}: {e}")

conn.close()

print("\nDatabase loading complete.")
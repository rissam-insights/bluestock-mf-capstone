import pandas as pd
from pathlib import Path

# Path to raw data folder
data_path = Path("data/raw")

# Read all Excel files
files = list(data_path.glob("*.xlsx"))

print(f"Total files found: {len(files)}\n")

for file in files:
    print("=" * 60)
    print(f"FILE: {file.name}")

    try:
        df = pd.read_excel(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\n")

    except Exception as e:
        print(f"Error reading {file.name}: {e}")
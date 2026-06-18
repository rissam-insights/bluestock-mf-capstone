import pandas as pd

df = pd.read_excel("data/raw/companies.xlsx", header=1)

print("\nMissing Values:\n")
print(df.isnull().sum())

print("\nDuplicate Rows:\n")
print(df.duplicated().sum())

print("\nUnique Companies:\n")
print(df["company_name"].nunique())
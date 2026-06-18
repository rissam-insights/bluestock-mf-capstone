import pandas as pd

df = pd.read_excel("data/raw/companies.xlsx", header=1)

print("\nColumns:\n")
print(df.columns)

print("\nShape:\n")
print(df.shape)

print("\nFirst 5 rows:\n")
print(df.head())
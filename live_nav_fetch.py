
import requests
import pandas as pd

# HDFC Top 100 Direct
scheme_code = "125497"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    print(nav_df.head())

    nav_df.to_csv(
        "data/raw/hdfc_top100_nav.csv",
        index=False
    )

    print("NAV data saved successfully!")

else:
    print("Failed to fetch data")
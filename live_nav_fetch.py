import pandas as pd
import requests
import os

URL = "https://api.mfapi.in/mf/125497"

os.makedirs("data/raw", exist_ok=True)

print("Fetching NAV data...")

response = requests.get(URL)

if response.status_code == 200:

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    output_file = "data/raw/live_nav_hdfc_top100.csv"

    nav_df.to_csv(output_file, index=False)

    print("Saved successfully!")
    print("Rows:", len(nav_df))
    print("File:", output_file)

else:
    print("Failed to fetch data")
    print("Status Code:", response.status_code)
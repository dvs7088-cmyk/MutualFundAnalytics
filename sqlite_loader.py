import pandas as pd
from sqlalchemy import create_engine
import os

print("Loading datasets into SQLite...")

engine = create_engine("sqlite:///bluestock_mf.db")

processed_path = "data/processed"

for file in os.listdir(processed_path):
    if file.endswith(".csv"):
        table_name = file.replace(".csv", "")

        df = pd.read_csv(os.path.join(processed_path, file))

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded: {table_name} ({len(df)} rows)")

print("Database created successfully!")


df.to_sql(
    table_name,
    engine,
    if_exists="replace",
    index=False,
    chunksize=5000,
    method="multi"
)

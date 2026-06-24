import pandas as pd
import os

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

print("Data Cleaning Started...")

for file_name in os.listdir(RAW_PATH):

    if file_name.endswith(".csv"):

        file_path = os.path.join(RAW_PATH, file_name)

        df = pd.read_csv(file_path)

        df.drop_duplicates(inplace=True)

        for column in df.columns:

            if df[column].dtype == "object":
                df[column] = df[column].fillna("Unknown")

            elif pd.api.types.is_numeric_dtype(df[column]):
                df[column] = df[column].fillna(df[column].median())

        output_file = os.path.join(PROCESSED_PATH, file_name)

        df.to_csv(output_file, index=False)
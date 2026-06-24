import os
import glob
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw")

csv_files = glob.glob(os.path.join(DATA_PATH, "*.csv"))

print("Total CSV Files Found:", len(csv_files))

for file in csv_files:
    print("\n" + "="*50)
    print("File:", os.path.basename(file))

    df = pd.read_csv(file)

    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())
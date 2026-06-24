import pandas as pd
from pathlib import Path

csv_files = list(Path(".").glob("*.csv"))

print("=" * 70)
print("DATA VALIDATION REPORT")
print("=" * 70)

for file in csv_files:
    df = pd.read_csv(file)

    print(f"\nDataset: {file.name}")
    print("-" * 50)

    print("Shape:", df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())
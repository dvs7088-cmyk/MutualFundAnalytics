import pandas as pd

print("=" * 60)
print("MUTUAL FUND ANALYTICS - EDA")
print("=" * 60)

# Load datasets
fund_master = pd.read_csv("data/processed/01_fund_master.csv")
scheme_perf = pd.read_csv("data/processed/07_scheme_performance.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions.csv")

# Total Funds
print("\nTotal Funds:", len(fund_master))

# Fund Categories
print("\nFund Categories:")
print(fund_master["category"].value_counts())

# Top 5 Fund Houses
print("\nTop Fund Houses:")
print(fund_master["fund_house"].value_counts().head())

# Average Returns
print("\nAverage 1 Year Return:")
print(round(scheme_perf["return_1yr_pct"].mean(), 2), "%")

print("\nAverage 3 Year Return:")
print(round(scheme_perf["return_3yr_pct"].mean(), 2), "%")

# Transaction Summary
print("\nTransaction Types:")
print(transactions["transaction_type"].value_counts())

# Total Investment Amount
print("\nTotal Transaction Amount:")
print(f"₹ {transactions['amount_inr'].sum():,}")

print("\nEDA Completed Successfully!")
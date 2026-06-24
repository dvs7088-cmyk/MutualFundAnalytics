-- 1. Top 5 Funds by AUM
SELECT amfi_code, scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by Fund
SELECT amfi_code,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Total Transactions by State
SELECT state,
       COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;

-- 4. Funds with Expense Ratio Below 1%
SELECT amfi_code,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Transaction Volume by Type
SELECT transaction_type,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- 6. Top 10 Cities by Investment Amount
SELECT city,
       SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY city
ORDER BY total_investment DESC
LIMIT 10;

-- 7. Highest Sharpe Ratio Funds
SELECT amfi_code,
       sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 8. Risk Grade Distribution
SELECT risk_grade,
       COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade;

-- 9. Average Investment by Payment Mode
SELECT payment_mode,
       AVG(amount_inr) AS avg_investment
FROM fact_transactions
GROUP BY payment_mode;

-- 10. Top 5 Fund Houses by AUM
SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM fact_performance
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;
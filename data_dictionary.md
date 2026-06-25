\# Mutual Fund Analytics - Data Dictionary



\## Project Overview



This project analyzes mutual fund performance, NAV trends, investor transactions, AUM growth, and portfolio holdings using Python, SQL, and SQLite.



\## 01\_fund\_master.csv



| Column       | Data Type | Description                   |

| ------------ | --------- | ----------------------------- |

| amfi\_code    | Integer   | Unique mutual fund identifier |

| fund\_house   | Text      | Mutual fund company           |

| scheme\_name  | Text      | Scheme name                   |

| category     | Text      | Fund category                 |

| sub\_category | Text      | Fund sub-category             |



\## 02\_nav\_history.csv



| Column    | Data Type | Description     |

| --------- | --------- | --------------- |

| amfi\_code | Integer   | Fund identifier |

| nav\_date  | Date      | NAV date        |

| nav       | Float     | Net Asset Value |



\## 03\_aum\_by\_fund\_house.csv



| Column     | Data Type | Description                       |

| ---------- | --------- | --------------------------------- |

| fund\_house | Text      | Fund house name                   |

| aum\_crore  | Float     | Assets Under Management (Crore ₹) |



\## 07\_scheme\_performance.csv



| Column            | Data Type | Description                  |

| ----------------- | --------- | ---------------------------- |

| return\_1yr\_pct    | Float     | 1-year return percentage     |

| return\_3yr\_pct    | Float     | 3-year return percentage     |

| return\_5yr\_pct    | Float     | 5-year return percentage     |

| expense\_ratio\_pct | Float     | Expense ratio percentage     |

| sharpe\_ratio      | Float     | Risk-adjusted return measure |

| risk\_grade        | Text      | Risk category                |



\## 08\_investor\_transactions.csv



| Column           | Data Type | Description                |

| ---------------- | --------- | -------------------------- |

| investor\_id      | Text      | Unique investor identifier |

| transaction\_type | Text      | SIP / Lumpsum / Redemption |

| amount\_inr       | Float     | Transaction amount in INR  |

| state            | Text      | Investor state             |

| city             | Text      | Investor city              |

| payment\_mode     | Text      | Mode of payment            |

| kyc\_status       | Text      | KYC verification status    |



\## Source Files



\* AMFI Mutual Fund Data

\* NAV History Data

\* Investor Transaction Dataset

\* Scheme Performance Dataset

\* Portfolio Holdings Dataset



\## Database



Database Name: bluestock\_mf.db



\## Author



Varsha Sri




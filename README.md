Wallet Risk Scoring – DeFi Protocol Data (Compound V2/V3):

Project Overview:
This project builds a risk scoring system for cryptocurrency wallets based on on-chain activity in Compound V2 and V3 protocols.
It assigns a score from 0 (highest risk) to 1000 (lowest risk) by analyzing lending, borrowing, and liquidation history.
The goal is to evaluate wallet creditworthiness for DeFi applications such as lending, risk management, and fraud detection.

Key Features:
1. On-chain Data Collection – Fetches transaction history using Web3.py and Compound protocol APIs.
2. Feature Engineering – Calculates metrics like collateral ratio, liquidation history, and borrow trends.
3. Risk Scoring Model – Applies a weighted algorithm to classify wallets into risk tiers (Low, Medium, High).
4. Clean Data Pipeline – Filters out unrelated or noisy transactions for protocol relevance.

Tech Stack:
Languages: Python
Libraries: Pandas, NumPy, Web3.py, Requests, scikit-learn
Data Source: Compound V2/V3 protocol (Ethereum)
Additional API: Covalent API for historical on-chain data

How It Works:
1. Fetch wallet transactions from Compound smart contracts

2. Filter protocol-specific activity (lending/borrowing interactions)

3. Engineer features:
Collateral-to-debt ratio
Liquidation count
Borrow amount volatility
Activity frequency (time between transactions)
Asset diversity

4. Normalize features with MinMaxScaler for fair comparison

5. Apply scoring logic:
Weighted combination of features → score between 0–1000

6. Export results as a CSV with wallet addresses, scores, and categories

Output Format: CSV:
Output – Generates a CSV file with wallet addresses, scores, and risk categories
1. Used the [Covalent API](https://www.covalenthq.com/) to retrieve historical on-chain transactions for each wallet  
2. Focused specifically on **Compound V2/V3** lending and borrowing interactions  
3. Filtered out unrelated or noisy transaction data to ensure protocol relevance

| Wallet Address | Risk Score | Risk Category |
| -------------- | ---------- | ------------- |
| 0xABC...123    | 220        | Low           |
| 0xDEF...456    | 670        | Medium        |
| 0xXYZ...789    | 920        | High          |


Risk Indicators:
* High borrow relative to supply → Risky
* Frequent liquidations → Risky
* Low transaction volume / long inactivity → Moderate risk
* Consistent repayments & multiple asset usage → Lower risk

File Structure:
wallet-risk-scoring/
├── data/ # Raw & processed data files
│
├── src/ # All Python scripts
│ ├── fetch_transactions.py
│ ├── features.py
│ └── risk_scoring.py
│
├── wallet_scores.csv # Final submission output
└── README.md # This file


* Notes:
1. The scoring model is simple and interpretable, prioritizing wallet behavior over prediction complexity  
2.  This structure can be expanded with on-chain credit models, anomaly detection, or DeFi lending health metrics  


 







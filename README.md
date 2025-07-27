 Wallet Risk Scoring (Compound V2/V3):

This project analyzes on-chain transactions from the Compound V2/V3 protocols and assigns risk scores to Ethereum wallets on a scale of 0 to 1000. It was built as part of the Round 2 Wallet Risk Scoring Challenge.

* Deliverables:
1. wallet_scores.csv — Final risk scores for all wallets  
2. README.md — Project overview, data collection details, feature explanation, and scoring logic

* Data Collection:
1. Used the [Covalent API](https://www.covalenthq.com/) to retrieve historical on-chain transactions for each wallet  
2. Focused specifically on **Compound V2/V3** lending and borrowing interactions  
3. Filtered out unrelated or noisy transaction data to ensure protocol relevance

* Feature Engineering:
Key features extracted to evaluate wallet behavior:

1. Number of borrow/lend transactions  
2. Net supply vs borrow amounts 
3. Liquidation history
4. Time between transactions (activity frequency)  
5. Diversity of assets interacted with

* Scoring Method:

1. Normalization :  
   All features were normalized using MinMaxScaler from sklearn to ensure fair comparison across metrics

2. Scoring Logic :
   A weighted combination of normalized features was used to calculate the final score:  
   0 = highest risk, 1000 = lowest risk

* Risk Indicators:
Features contributing to the risk assessment:

1. High borrow relative to supply → Risky  
2. Frequent liquidations → Risky  
3. Long inactivity or low transaction volume → Moderate risk  
4. Consistent repayments & interaction with multiple assets → Lower risk

* File Structure:
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


 Round 2 Wallet Risk Scoring Challenge.






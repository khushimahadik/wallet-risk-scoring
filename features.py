import json
import pandas as pd
from collections import defaultdict


def load_data(path="data/fetched_data.json"):
    with open(path, "r") as f:
        return json.load(f)


def extract_features(wallet_data):
    features = defaultdict(list)

    for entry in wallet_data:
        wallet = entry.get("wallet")
        data = entry.get("data", {})
        txns = data.get("items", [])
        total_txns = len(txns)
        failed_txns = sum(1 for tx in txns if tx.get("success") is False)
        compound_txns = [
            tx
            for tx in txns
            if "compound"
            in tx.get("log_events", [{}])[0].get("decoded", {}).get("name", "").lower()
        ]
        compound_interactions = len(compound_txns)

        features["wallet_id"].append(wallet)
        features["total_txns"].append(total_txns)
        features["failed_txns"].append(failed_txns)
        features["compound_interactions"].append(compound_interactions)

    return pd.DataFrame(features)


def main():
    raw_data = load_data()
    df = extract_features(raw_data)
    df.to_csv("data/features.csv", index=False)
    print("✅ Features saved to data/features.csv")


if __name__ == "__main__":
    main()

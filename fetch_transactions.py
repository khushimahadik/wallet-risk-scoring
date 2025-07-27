import os
import csv
import json
import requests


COVALENT_API_KEY = "cqt_rQ9QCfQcVpkWqKWPKbPQwytccrmh"
CHAIN_ID = "1"

INPUT_CSV_PATH = "data/Wallets.csv"
OUTPUT_JSON_PATH = "data/fetched_data.json"


def fetch_token_balances(wallet_address):
    url = f"https://api.covalenthq.com/v1/{CHAIN_ID}/address/{wallet_address}/balances_v2/?key={COVALENT_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {"wallet": wallet_address, "tokens": data["data"]["items"]}
    else:
        print(f"❌ Error {response.status_code} for wallet {wallet_address}")
        return {"wallet": wallet_address, "error": response.text}


def main():
    if not os.path.exists(INPUT_CSV_PATH):
        print(f"❌ CSV file not found at {INPUT_CSV_PATH}")
        return

    results = []

    with open(INPUT_CSV_PATH, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        wallet_ids = [
            row["wallet_id"].strip() for row in reader if row.get("wallet_id")
        ]

    print(f"📦 Fetching token balances for {len(wallet_ids)} wallets...")

    for wallet in wallet_ids:
        print(f"🔄 {wallet}")
        result = fetch_token_balances(wallet)
        results.append(result)

    # Save to JSON
    os.makedirs("data", exist_ok=True)
    with open(OUTPUT_JSON_PATH, "w") as outfile:
        json.dump(results, outfile, indent=2)

    print(f"\n✅ Done! Data saved to {OUTPUT_JSON_PATH}")


if __name__ == "__main__":
    main()

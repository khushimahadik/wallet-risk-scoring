import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def load_features(file_path="data/features.csv"):
    return pd.read_csv(file_path)


def score_wallets(df):
    feature_columns = [col for col in df.columns if col != "wallet_id"]
    scaler = MinMaxScaler()
    df_scaled = pd.DataFrame(
        scaler.fit_transform(df[feature_columns]), columns=feature_columns
    )
    df_scaled["score"] = (df_scaled.sum(axis=1) / len(feature_columns) * 1000).astype(
        int
    )
    df_final = pd.DataFrame({"wallet_id": df["wallet_id"], "score": df_scaled["score"]})
    return df_final


def main():
    df = load_features()
    scores = score_wallets(df)
    print("📦 Columns in your CSV:")
    print(scores.columns.tolist())
    scores.to_csv("data/scores.csv", index=False)
    print("✅ Saved: data/scores.csv")


if __name__ == "__main__":
    main()

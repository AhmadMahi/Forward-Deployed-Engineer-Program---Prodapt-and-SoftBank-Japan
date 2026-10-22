"""SmartDesk step 13: import legacy tickets from a messy CSV (extract, transform, load)."""
import sqlite3
from pathlib import Path

import pandas as pd

LEGACY = Path(__file__).resolve().parents[1] / "data" / "legacy_tickets.csv"
CATEGORY = {"network": "network", "billing": "billing", "account": "account", "other": "other"}
PRIORITY = {"high": "high", "med": "medium", "medium": "medium", "low": "low"}


def extract(path=LEGACY):
    return pd.read_csv(path, dtype=str)


def transform(df):
    """Clean, validate and de-duplicate. Returns (clean, rejected)."""
    df = df.rename(columns={"Ticket ID": "legacy_id", "Customer Name": "customer", "Type": "category",
                            "Prio": "priority", "Status": "status", "Description": "body", "Opened": "created_at"})
    df = df.apply(lambda c: c.str.strip())          # every column is read as text
    df = df.drop_duplicates()
    df["category"] = df["category"].str.lower().map(CATEGORY)
    df["priority"] = df["priority"].str.lower().map(PRIORITY)
    df["status"] = df["status"].str.lower()
    df["created_at"] = pd.to_datetime(df["created_at"], dayfirst=True, errors="coerce", format="mixed")
    bad = df["customer"].isna() | df["body"].isna() | df["created_at"].isna() | df["category"].isna()
    return df[~bad].reset_index(drop=True), df[bad].reset_index(drop=True)


def load(df, db_path):
    with sqlite3.connect(db_path) as con:
        df.assign(created_at=df["created_at"].dt.strftime("%Y-%m-%d")).to_sql(
            "legacy_tickets", con, if_exists="replace", index=False)
    return len(df)


def quality_report(clean, rejected):
    return {"loaded": len(clean), "rejected": len(rejected),
            "missing_values": int(clean.isna().sum().sum()),
            "duplicate_ids": int(clean["legacy_id"].duplicated().sum())}


if __name__ == "__main__":
    clean, rejected = transform(extract())
    load(clean, "smartdesk.db")
    print(quality_report(clean, rejected))

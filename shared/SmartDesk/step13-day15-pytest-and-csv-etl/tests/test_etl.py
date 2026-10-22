import sqlite3

import pandas as pd
import pytest

from etl_import import extract, load, quality_report, transform


@pytest.fixture
def result():
    return transform(extract())


def test_duplicates_removed_and_bad_rows_rejected(result):
    clean, rejected = result
    assert clean["legacy_id"].is_unique
    assert set(rejected["legacy_id"]) == {"104", "105", "106"}


def test_values_normalised(result):
    clean, _ = result
    assert set(clean["priority"]) <= {"low", "medium", "high"}
    assert clean.loc[clean["legacy_id"] == "101", "customer"].item() == "Aiko Tanaka"


@pytest.mark.parametrize("raw,expected", [("26/10/2026", "2026-10-26"), ("2026-10-26", "2026-10-26")])
def test_mixed_date_formats(raw, expected):
    df = pd.DataFrame([{"Ticket ID": "1", "Customer Name": "A", "Type": "billing", "Prio": "low",
                        "Status": "open", "Description": "x", "Opened": raw}])
    clean, _ = transform(df)
    assert clean["created_at"].dt.strftime("%Y-%m-%d").item() == expected


def test_load_and_quality(result, tmp_path):
    clean, rejected = result
    db = tmp_path / "t.db"
    assert load(clean, db) == len(clean)
    with sqlite3.connect(db) as con:
        assert con.execute("select count(*) from legacy_tickets").fetchone()[0] == len(clean)
    assert quality_report(clean, rejected)["duplicate_ids"] == 0

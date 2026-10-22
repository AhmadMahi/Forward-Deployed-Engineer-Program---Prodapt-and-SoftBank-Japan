"""Characterisation tests: they record what the legacy importer does today, quirks included.
Keep them green while you modernise the module. Change one only on purpose, and say why in your PR."""
from ticketing import legacy_csv_import as legacy
from ticketing import db, service


def test_skips_comments_blank_and_short_lines():
    assert legacy.parse_line("# header") is None
    assert legacy.parse_line("   ") is None
    assert legacy.parse_line("bad line without enough fields") is None


def test_normalises_fields():
    row = legacy.parse_line("aiko tanaka;09012345678;Network;1;No signal at home")
    assert row["customer"] == "Aiko Tanaka"
    assert row["msisdn"] == "+819012345678"
    assert row["category"] == "network"
    assert row["priority"] == "high"
    assert row["body"] == "No signal at home"


def test_keeps_international_numbers():
    assert legacy.parse_line("r;+819098765432;billing;2;x")["msisdn"] == "+819098765432"


def test_quirks_are_preserved():
    assert legacy.parse_line("k;070;;2;a")["category"] == "other"           # empty category
    assert legacy.parse_line("s;090;billing;9;a")["priority"] == "medium"   # unknown priority
    assert legacy.parse_line("k;070;network;2;Roaming; tried restart")["body"] == "Roaming; tried restart"


def test_created_at_format():
    created = legacy.parse_line("a;090;network;1;x")["created_at"]
    assert len(created) == 19 and created[4] == "-" and created[13] == ":"


def test_import_file_counts(legacy_csv):
    rows = legacy.import_file(legacy_csv)
    assert len(rows) == 5
    assert [r["priority"] for r in rows] == ["high", "medium", "low", "medium", "medium"]


def test_import_into_db(conn, legacy_csv):
    assert service.import_legacy(conn, legacy_csv) == 5
    assert len(db.list_tickets(conn, status="open")) == 5

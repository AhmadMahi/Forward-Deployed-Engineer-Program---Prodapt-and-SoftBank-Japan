"""Characterisation tests: written against the legacy module first, then run against the modern one."""
import sqlite3

import pytest

from legacy import csv_import_legacy as legacy
from modern import csv_import as modern

GOOD = ["id,customer,priority,body", "1,Aiko Tanaka,1,No signal", "2,Rahul Mehta,2,Charged twice",
        "3,Kenji Sato,3,Login fails"]


def rows(db):
    with sqlite3.connect(db) as con:
        return con.execute("select * from tickets order by id").fetchall()


def test_same_output_for_valid_rows(tmp_path):
    a, b = tmp_path / "a.db", tmp_path / "b.db"
    assert legacy.import_rows(str(a), GOOD) == modern.import_rows(str(b), GOOD).imported == 3
    assert rows(a) == rows(b)


def test_modern_blocks_sql_injection(tmp_path):
    db = tmp_path / "m.db"
    evil = GOOD[:2] + ["9,x'); drop table tickets; --,1,boom"]
    modern.import_rows(str(db), evil)
    assert len(rows(db)) == 2 and rows(db)[1][1].startswith("x'")


def test_modern_never_evals_input(tmp_path):
    r = modern.import_rows(str(tmp_path / "e.db"), ["h", "1,A,__import__('os').getcwd(),x"])
    assert r.imported == 0 and r.rejected


@pytest.mark.parametrize("bad", ["only,two", "x,A,1,body", "1,A,9,body"])
def test_bad_rows_are_reported_not_hidden(tmp_path, bad):
    r = modern.import_rows(str(tmp_path / "r.db"), ["h", bad])
    assert r.imported == 0 and len(r.rejected) == 1

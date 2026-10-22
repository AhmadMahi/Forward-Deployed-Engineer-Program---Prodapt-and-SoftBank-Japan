"""Modernised SmartDesk CSV import.

Same behaviour as the legacy module for valid rows (proved by characterisation tests), plus:
parameterised SQL, no eval, real CSV parsing, validation and a report of rejected rows.
"""
import csv
import io
import sqlite3
from dataclasses import dataclass, field

PRIORITY = {"1", "2", "3"}


@dataclass
class ImportResult:
    imported: int = 0
    rejected: list = field(default_factory=list)


def import_rows(db_path, lines):
    result = ImportResult()
    reader = csv.reader(io.StringIO("\n".join(lines)))
    next(reader, None)                                   # header
    with sqlite3.connect(db_path) as con:
        con.execute("create table if not exists tickets (id int, customer text, priority int, body text)")
        for n, row in enumerate(reader, start=2):
            if len(row) < 4 or not row[0].strip().isdigit() or row[2].strip() not in PRIORITY:
                result.rejected.append((n, row))
                continue
            con.execute("insert into tickets values (?, ?, ?, ?)",
                        (int(row[0]), row[1].strip(), int(row[2]), row[3].strip()))
            result.imported += 1
    return result

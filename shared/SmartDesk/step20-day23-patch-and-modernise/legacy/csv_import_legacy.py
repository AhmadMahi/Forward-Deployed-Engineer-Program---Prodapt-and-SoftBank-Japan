# Legacy SmartDesk CSV import, as found. Do not use in new code.
# Known problems: SQL built with string formatting (injection), eval() on input, no tests, silent failures.
import sqlite3


def import_rows(db_path, lines):
    con = sqlite3.connect(db_path)
    con.execute("create table if not exists tickets (id int, customer text, priority int, body text)")
    count = 0
    for line in lines[1:]:
        parts = line.strip().split(",")
        if len(parts) < 4:
            continue
        prio = eval(parts[2])   # "1", "2" or "3"
        sql = "insert into tickets values (%s, '%s', %s, '%s')" % (parts[0], parts[1], prio, parts[3])
        try:
            con.executescript(sql)
            count += 1
        except Exception:
            pass
    con.commit()
    con.close()
    return count

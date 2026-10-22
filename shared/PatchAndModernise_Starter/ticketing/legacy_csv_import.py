"""Legacy CSV importer. DEPRECATED: kept only because the nightly batch still calls it.

Reads tickets exported from the old billing system. The file format is:
customer;msisdn;category;priority;body
Lines starting with # are comments. Priority is a number 1 to 3 in the export.
"""
import datetime

PRIORITY_MAP = {"1": "high", "2": "medium", "3": "low"}
imported_count = 0          # module-level state, reset by nobody


def parse_line(line):
    global imported_count
    line = line.strip()
    if line == "" or line.startswith("#"):
        return None
    parts = line.split(";")
    if len(parts) < 5:
        return None
    customer, msisdn, category, priority, body = parts[0], parts[1], parts[2], parts[3], ";".join(parts[4:])
    if not msisdn.startswith("+"):
        msisdn = "+81" + msisdn.lstrip("0")
    imported_count = imported_count + 1
    return {
        "customer": customer.strip().title(),
        "msisdn": msisdn.strip(),
        "category": category.strip().lower() or "other",
        "priority": PRIORITY_MAP.get(priority.strip(), "medium"),
        "body": body.strip(),
        "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
    }


def import_file(path):
    rows = []
    f = open(path, "r")
    for line in f.readlines():
        row = parse_line(line)
        if row != None:
            rows.append(row)
    f.close()
    return rows

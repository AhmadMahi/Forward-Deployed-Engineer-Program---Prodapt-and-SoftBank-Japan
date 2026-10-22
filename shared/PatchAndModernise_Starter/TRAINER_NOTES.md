# Trainer notes: Patch and Modernise answer key

For trainers only. Do not share with learners before the Day 25 review.

## Planted findings

| ID | Tool | Finding | File | Suggested severity | Expected fix | Proving test |
|---|---|---|---|---|---|---|
| F1 | pip-audit | `PyJWT==1.7.1` is affected by CVE-2022-29217 (algorithm confusion; fixed in PyJWT 2.4.0) | `requirements.txt` | High | Upgrade to a current PyJWT 2.x release. In 2.x `jwt.encode` returns `str`, so remove `.decode("utf-8")` in `auth.issue_token`. | `test_token_round_trip` must still pass after the upgrade; add a test that a token signed with `alg: none` is rejected. |
| F2 | bandit B105 | Hard-coded signing secret | `ticketing/auth.py` | High | Read `TELCODESK_SECRET` from the environment; fail fast if missing in production. | Test that `issue_token` uses the environment value (monkeypatch). |
| F3 | bandit B608 | SQL built with string formatting in `find_by_customer` | `ticketing/db.py` | High | Parameterised query `WHERE customer = ?`. | Test that `"x' OR '1'='1"` returns no rows. |
| F4 | bandit B602 (and B404) | `subprocess.call(..., shell=True)` with an untrusted host | `ticketing/diagnostics.py` | Medium (High if reachable from user input) | Validate the host (IP or hostname pattern) and call `subprocess.run(["ping", "-c", str(count), host])` without a shell. | Test that `"8.8.8.8; rm -rf /"` raises `ValueError`. |
| F5 | npm audit | `express` 4.17.1 and several of its dependencies have published advisories. The exact list depends on the advisory database on the day. | `notifier/package.json` | Moderate to High | Upgrade express to the latest 4.x (or 5.x with care), regenerate the lockfile, re-run `npm audit`. | `node test.js` still passes. |
| F6 | Review | Token lifetime of 30 days | `ticketing/auth.py` | Medium | Short-lived tokens (for example 15 minutes) with scopes, as taught on Day 7. | Test that an expired token is rejected. |

F6 is not found by any scanner. Give credit to learners who find it by reading the code: that is the point of human review.

## Modernisation target

`ticketing/legacy_csv_import.py`:
- Uses `datetime.datetime.utcnow()`, deprecated since Python 3.12. Replace with `datetime.datetime.now(datetime.timezone.utc)`.
- Hand-rolled `split(";")` instead of the `csv` module with `delimiter=";"`.
- Module-level `imported_count` global.
- `open()` without a context manager, `!= None` comparison.

Good migrations keep every test in `tests/test_legacy_import.py` green, including the quirks: empty category becomes `other`, unknown priority becomes `medium`, extra `;` stay in the body. Strong submissions add a FastAPI upload endpoint behind the same parsing function and keep the CLI working.

Note: PyJWT 1.7.1 itself calls `utcnow()`, so learners see DeprecationWarnings from the library too. They disappear after the F1 upgrade. A good report notices this.

## Marking guide

| Criterion | Points | What full marks look like |
|---|---|---|
| Findings identified and correctly rated | 25 | F1 to F5 found, severities justified, F6 found by review |
| Fixes work and are proven by tests | 30 | Every fix has a test that fails before and passes after; scans re-run and clean (or residual risk explained) |
| Modernisation done in safe, verified steps | 25 | Small commits, characterisation tests green at every step, no behaviour change without a note |
| Clarity of report and service note | 20 | Report complete; note explains the approach, risks and how it would run as a repeatable service with SLAs |

## Environment notes

- `pip-audit` and `npm audit` need internet access. If the network is blocked, accept the trainer-provided scan output.
- `notifier/package-lock.json` is committed so `npm audit` works without installing packages. `node_modules` is not committed.

# TelcoDesk Legacy: Patch and Modernise starter

Starter repository for the **Day 23 Patch and Modernise assignment** (NEW (v4)). Due **Day 25, 09:30**. Reviewed in the Day 25 opening slot.

TelcoDesk Legacy is a small ticketing app for a telecom support team. It was written years ago, it works, and nobody has touched it since. Your job is to treat it like a real customer system: find what is unsafe or outdated, fix it with OpenAI Codex as your assistant, and prove every change with tests.

## What is inside

| Path | What it is |
|---|---|
| `ticketing/db.py` | SQLite storage for tickets |
| `ticketing/auth.py` | Agent login tokens for the support console |
| `ticketing/diagnostics.py` | Network diagnostics used by tier-2 support |
| `ticketing/legacy_csv_import.py` | The **deprecated** nightly CSV importer (your modernisation target) |
| `ticketing/service.py` | Business logic |
| `ticketing/cli.py` | Command line entry point |
| `notifier/` | A small Node.js (Express) notification stub |
| `data/legacy_tickets.csv` | A sample export from the old billing system |
| `tests/` | pytest tests. They all pass today. |

## Run it

```bash
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q                  # all tests should pass before you change anything
python -m ticketing.cli import data/legacy_tickets.csv
python -m ticketing.cli list
```

Notifier (needs Node.js LTS):

```bash
cd notifier
node test.js
npm ci --ignore-scripts              # only if you want to run the server: npm start
```

## The assignment

1. **Scan.** Run `bandit -r ticketing`, `pip-audit -r requirements.txt` and, in `notifier/`, `npm audit`. Save the raw output.
2. **Report.** Fill in the vulnerability report template (`shared/templates/Vulnerability_Report_Template.md`): finding, severity, affected file, proposed fix, verified (yes or no).
3. **Patch.** Use OpenAI Codex to propose patches. For each fix, add or update a test that proves it. Re-run the scans and record the "after" results.
4. **Modernise.** Pick one legacy module (`ticketing/legacy_csv_import.py` is the suggested one). The characterisation tests in `tests/test_legacy_import.py` record what it does today. Keep them green while you migrate it in small, verified steps (for example to the `csv` module, timezone-aware dates, no global state, and a FastAPI upload endpoint).
5. **Explain.** Write a one-page note: your patching and modernisation approach, the risks, and what you would offer a customer as a service.
6. **Submit.** A pull request plus the report and the note.

## Rubric

| Rubric criterion | Points |
|---|---|
| Findings identified and correctly rated | 25 |
| Fixes work and are proven by tests | 30 |
| Modernisation done in safe, verified steps | 25 |
| Clarity of report and service note | 20 |
| **Total** | **100** |

## Rules

- Work on a branch. Small commits. One pull request.
- Read every diff Codex proposes. Accept only code you can explain.
- Never paste secrets into prompts. Move the hard-coded secret out of the code as part of your fix.
- Keep the characterisation tests green. If you change one on purpose, say why in the pull request.
- Use the program's approved model at default reasoning effort. Note the tokens you used.

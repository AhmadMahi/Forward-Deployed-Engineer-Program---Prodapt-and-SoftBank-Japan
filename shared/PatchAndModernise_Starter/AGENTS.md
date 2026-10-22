# AGENTS.md: TelcoDesk Legacy

## Project
A small legacy telecom ticketing app (Python 3.12 or newer) with a Node.js notifier stub. Used for the Patch and Modernise assignment.

## Commands
- Install: `pip install -r requirements.txt`
- Test: `python -m pytest -q`
- Security scans: `bandit -r ticketing`, `pip-audit -r requirements.txt`, `cd notifier && npm audit`
- Notifier test: `cd notifier && node test.js`

## Style
- Python: standard library first, type hints on new code, small functions, no global state.
- Every behaviour change needs a test. Every security fix needs a test that would have failed before the fix.

## Do not touch
- `tests/test_legacy_import.py`: characterisation tests. Keep them green. Change one only when the learner asks, and explain why.
- `data/legacy_tickets.csv`: sample input. Do not edit it to make a test pass.

## Safety
- Never put secrets in prompts, code or this file. Read secrets from environment variables.
- Do not run `ticketing.diagnostics.ping_host` with `dry_run=False`.
- Propose a plan before changing more than one file. Make small, reviewable changes.

# Day 23 Hotel Lab: Industry Use Cases and Agentic Security

**Total time:** 80 to 90 minutes | **Day:** Thu 26 Nov 2026 | **Track:** GenAI (SME session) | NEW (v4)

## Before you start

- Steps 2 and 3 run in **VS Code** on your laptop, because the scanners work on a real repository. The notebook (`Day23_Industry_Use_Cases_and_Agentic_Security_SME_Colab.ipynb`) is an optional browser alternative for practice.
- `pip-audit` and `npm audit` need internet access. `bandit` and the tests run offline.
- No API key needed tonight. If you use Codex, use the approved model and never paste secrets or customer data into a prompt.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 20 min | Read the SME notes (post-read) and the industry use cases one-pager. | `Day23_PostRead_Industry_Use_Cases_and_Agentic_Security_SME_Recap_and_Beyond.pdf`, `Day23_Industry_Use_Cases_OnePager.pdf` |
| 2 | 45 min | Start the Patch and Modernise assignment on the starter repo in VS Code: run `python -m pytest -q`, then `bandit -r ticketing`, `pip-audit -r requirements.txt` and, in `notifier/`, `npm audit`. Log every finding in the vulnerability report template. | `shared/PatchAndModernise_Starter/README.md`, `shared/templates/Vulnerability_Report_Template.md` |
| 3 | 15 min | Map SmartDesk to a GenAI maturity level using the do's and don'ts checklist. List the three gaps that block the next level. | `Day23_Industry_Use_Cases_OnePager.pdf` |

## Submit

Your **draft vulnerability report** (findings logged, "verified" set to no until a test proves the fix). The final assignment is due **Day 25, 09:30**: pull request, final report and one-page service note.

## Stuck?

- `pip install -r requirements.txt` fails: create a fresh virtual environment with Python 3.12 or newer and try again.
- `npm audit` says it needs a lockfile: run it inside `notifier/`, where `package-lock.json` lives.
- `pip-audit` or `npm audit` cannot reach the internet: note it in the report and run them in class tomorrow morning.
- Not sure about a severity: ask "is this reachable from user input?" and write your reasoning in the report.
- Tests fail before you changed anything: check you are in the starter folder and on Python 3.12 or newer.

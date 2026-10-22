# AGENTS.md

Copy this file to the root of your repository and fill in the blanks. OpenAI Codex reads it before it works. Keep it short and up to date.

## Project

<One or two sentences: what this project is and who uses it.>

## Commands

- Install: `pip install -r requirements.txt` (and `npm install` in `frontend/` if you have one)
- Run: `uvicorn app.main:app --reload`
- Test: `pytest -q`
- Lint: `ruff check .`
- Security scan: `bandit -r app` and `pip-audit -r requirements.txt` (`npm audit` for JavaScript)

Run the tests after every change. A task is done only when the tests pass.

## Style

- Python 3.12, type hints, small functions, clear names.
- Pydantic models for every request and response.
- Short, plain comments only where the code is not obvious.

## Folders

- `app/`: application code. Edit here.
- `tests/`: tests. Add a test for every change.
- Do not touch: `.github/`, `migrations/`, `data/raw/`, `.env`, any lock file unless asked.

## Rules

- Never put secrets in prompts, code, tests or this file. Keys live in `.env` (git-ignored) or Colab Secrets.
- Never add a new dependency without saying why. Pin versions.
- Plan first for anything that touches more than one file. Work in small steps.
- Do not use full-access or bypass modes.
- Explain any change you cannot cover with a test.

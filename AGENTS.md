# AGENTS.md: FDE Program course repository

## Purpose
Course materials for the Prodapt Forward Deployed Engineer Program (40 days, v4). One folder per day.

## Structure
- `DayNN-Topic/` for Days 01 to 35, `Day36-40-Capstone/` for the capstone, `archive/v1-40-day/` for the previous version (read only).
- Each technical day folder holds 9 files: Deck, PreRead, PostRead, Colab notebook, App_Build_Prompts, HandsOn_Problem_Statements, Workbook, Quiz, Hotel_Lab.
- FDE Mindset day folders hold a README placeholder only. Do not edit them.

## Rules
- OpenAI only: OpenAI Codex as the AI coding tool, OpenAI APIs for LLM calls. Do not add other vendors' assistants or instruction files.
- Notebooks: Option A cells run in Colab, Option B cells (commented) are for VS Code. Every GenAI cell must still run in offline demo mode without a key.
- Default model comes from the `LLM_MODEL` environment variable; see `docs/MODEL_GUIDE.md`.
- Never commit secrets. Prices are placeholders and must be labelled as such.
- No em dashes. Short, plain sentences. Mark v4 additions with `NEW (v4)`.
- Before opening a pull request: every notebook runs top to bottom in offline mode; links in README resolve; no secrets in the diff.

## Commands
- Validate notebooks: `python tools/check_notebooks.py` (runs each notebook in offline mode).
- Check links: `python tools/check_links.py`.

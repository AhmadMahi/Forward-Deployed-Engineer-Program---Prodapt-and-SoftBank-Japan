# Day 6 Hotel Lab: SQLAlchemy, Relationships and API Docs

**Total time:** 105 to 120 minutes | **Day:** Mon 02 Nov 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- SQLite is a single file, so it works the same in Colab and VS Code. No database server is needed.
- If a cell complains that a table or row already exists, re-run the cell that deletes and recreates `library.db`.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day06_PostRead_SQLAlchemy_and_API_Docs_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom, then add a Comment model with a one-to-many relationship and test a rollback. | `Day06_SQLAlchemy_and_API_Docs_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (models, relationships, joins and transactions). Stretch set optional. | `Day06_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: SQLAlchemy code boxes (Section D). | `Day06_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 5: SQLite persistence and Swagger docs for SmartDesk. OpenAI Codex allowed; review every line. | `Day06_App_Build_Prompts.md` |

## Submit

A **Swagger screenshot** of your API's /docs page (in VS Code with uvicorn running, or the exported `openapi.json` paths list if you stayed in Colab).

## Stuck?

- `IntegrityError: UNIQUE constraint failed`: you ran the insert cell twice. Re-run the setup cell that deletes the database file.
- `DetachedInstanceError`: you used an object after its `Session` closed. Read what you need inside the `with Session(...)` block.
- A relationship list is empty: check `back_populates` names match on both classes.
- /docs does not show your summary: re-run the `%%writefile` cell and then the `importlib.reload(...)` cell.

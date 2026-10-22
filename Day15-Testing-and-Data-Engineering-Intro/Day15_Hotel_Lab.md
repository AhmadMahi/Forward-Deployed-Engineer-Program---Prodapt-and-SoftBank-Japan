# Day 15 Hotel Lab: Testing and Data Engineering Intro

**Total time:** 105 to 120 minutes | **Day:** Mon 16 Nov 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- If you have no API key, GenAI cells run in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day15_PostRead_Testing_and_Data_Engineering_Intro_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then add three PyTest cases with TestClient and ingest a messy CSV with pandas. | `Day15_Testing_and_Data_Engineering_Intro_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (testing and ETL). Stretch set optional. | `Day15_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: testing and data lifecycle questions. | `Day15_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 13: PyTest suite (Codex may draft tests; you review) and import legacy tickets. OpenAI Codex allowed; review every line. | `Day15_App_Build_Prompts.md` |

## Submit

Your **pytest output** (a screenshot or the copied text of `pytest -q`).

## Stuck?

- `ModuleNotFoundError: tickets_api`: run the `%%writefile` cells first; they create the files in the `day15` folder.
- Tests pass alone but fail together: a test changed shared data. Reset it in a fixture.
- `pd.to_datetime` complains about formats: use `format="mixed", dayfirst=True`.
- An AI-drafted test fails: check the rule before changing any code.

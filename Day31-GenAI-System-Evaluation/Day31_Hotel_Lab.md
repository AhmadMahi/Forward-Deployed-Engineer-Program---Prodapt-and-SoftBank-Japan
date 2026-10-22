# Day 31 Hotel Lab: GenAI System Evaluation

**Total time:** 105 to 120 minutes | **Day:** Tue 08 Dec 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- If you have no API key, GenAI cells run in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day31_PostRead_GenAI_System_Evaluation_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then add five questions to the golden set, compute faithfulness and relevance, and slice the results by category (topic and language). | `Day31_GenAI_System_Evaluation_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (evaluation metric and error analysis problems). Stretch problem optional. | `Day31_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: evaluation questions (Sections A to C). | `Day31_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 26: golden set and evaluation dashboard. OpenAI Codex allowed; review every line. | `Day31_App_Build_Prompts.md` |

## Submit

A **metrics table** (hit@3, MRR, faithfulness, correctness, overall and per slice) with **one error analysis**: a failure you read, its category (retrieval miss or generation error), the cause and the fix you would try first.

## Stuck?

- Japanese questions score 0 offline: expected. Offline embeddings only match shared words. Note it as a bias finding.
- Faithfulness is 1.0 for everything: check your generator is not returning "I don't know" (counted as faithful by design).
- `KeyError` when adding questions: every item needs `q`, `expect`, `source`, `topic` and `lang`. Use `None` as the source for unanswerable ones.
- pass^k looks too low: that is the point. Report it next to pass@k.

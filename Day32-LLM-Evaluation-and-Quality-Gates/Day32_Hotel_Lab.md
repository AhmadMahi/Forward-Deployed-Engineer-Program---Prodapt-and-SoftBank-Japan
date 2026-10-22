# Day 32 Hotel Lab: LLM Evaluation and Quality Gates

**Total time:** 105 to 120 minutes | **Day:** Wed 09 Dec 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- If you have no API key, GenAI cells run in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.
- Prices in the notebook are placeholders. Say so whenever you share a cost number.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day32_PostRead_LLM_Evaluation_and_Quality_Gates_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then add a regression test that fails when accuracy (pass rate) or cost per query worsens versus the v1 baseline. | `Day32_LLM_Evaluation_and_Quality_Gates_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (quality gate and regression problems). Stretch problem optional. | `Day32_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: QA questions (Sections A to C). | `Day32_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 27: quality gate in CI with cost metrics. OpenAI Codex allowed; review every line. | `Day32_App_Build_Prompts.md` |

## Submit

**Gate output** for two runs: one that passes and one that fails (on quality or cost), with the failure reasons printed by the gate.

## Stuck?

- `report_v1.json` not found: run the gate for `v1` first. Later versions compare against it.
- The tool-call test fails on `Refund 1,200 on ORD-9`: that is planted. Fix the amount parsing in `tools_under_test.py`.
- Cost numbers look tiny: they are per query with placeholder prices. Compare the percentage change, not the absolute value.
- `ModuleNotFoundError: jsonschema`: run the install cell again, then **Runtime > Restart session**.

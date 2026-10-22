# Day 34 Hotel Lab: LLM Deployment and Lifecycle

**Total time:** 105 to 120 minutes | **Day:** Fri 11 Dec 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- No API key? Every cell runs in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Azure deployment cells are for class only (Azure window 2). They are marked and print a message in Colab.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask on Monday. | `Day34_PostRead_LLM_Deployment_and_Lifecycle_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then run the gateway with streaming; simulate a canary release and rollback. | `Day34_LLM_Deployment_and_Lifecycle_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (deployment and versioning). Stretch problem optional. | `Day34_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: deployment questions. | `Day34_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 29: production gateway. OpenAI Codex allowed; review every line. | `Day34_App_Build_Prompts.md` |

## Submit

Your **rollback test notes**: the release you promoted, the metric that triggered the rollback (or the promote decision), and the exact rollback step you ran.

## Stuck?

- `ModuleNotFoundError`: run the install cell again, then **Runtime > Restart session**.
- The streaming cell hangs: another process may be using port 8034. Restart the session and run it again.
- Canary share is not exactly 10%: hashing gives close to 10% for 5,000 users. That is expected.
- The budget test returns 429 early: run the gateway cell again to reset the in-memory budget.

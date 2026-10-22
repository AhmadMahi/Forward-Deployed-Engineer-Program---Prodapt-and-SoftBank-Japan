# Day 7 Hotel Lab: FastAPI Advanced, Security and MongoDB

**Total time:** 105 to 120 minutes | **Day:** Tue 03 Nov 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- Colab uses `mongomock`, an in-memory MongoDB, so no database account is needed. MongoDB Atlas is optional.
- The `pip-audit` cell needs internet. If it fails, run it later in VS Code; everything else runs offline.
- Only test injection payloads against your own local code.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day07_PostRead_FastAPI_Advanced_Security_and_MongoDB_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom, then protect one route with JWT and try it with a valid, expired and missing token; run a Mongo aggregation. | `Day07_FastAPI_Advanced_Security_and_MongoDB_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (dependencies, middleware, JWT and MongoDB API problems). Stretch set optional. | `Day07_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: security and dependency injection questions. | `Day07_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 6: login with roles; analytics endpoint; run bandit and pip-audit. OpenAI Codex allowed; review every line. | `Day07_App_Build_Prompts.md` |

## Submit

Your **vulnerability report v1** (use `shared/templates/Vulnerability_Report_Template.md`): every bandit and pip-audit finding, with at least two fixed and marked verified with evidence.

## Stuck?

- 401 on every call: log in again; tokens expire after 15 minutes by design.
- 403 instead of 401: you are logged in, but the token lacks the scope or role. Check the `scope` claim.
- `InvalidId` or 404 for a ticket: the id must be a valid 24 character ObjectId string.
- bandit prints nothing: check the file path, and use `-f json` to see the full result.
- `pip-audit` hangs or fails: it needs internet. Note it in your report and run it in VS Code later.

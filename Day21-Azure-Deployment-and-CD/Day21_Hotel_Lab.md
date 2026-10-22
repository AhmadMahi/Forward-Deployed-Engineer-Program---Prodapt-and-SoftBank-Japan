# Day 21 Hotel Lab: Azure Deployment and Continuous Delivery

**Total time:** 105 to 120 minutes | **Day:** Tue 24 Nov 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- Azure steps run **in class only**, during the subscription window. Tonight everything runs offline, including the pipeline, Key Vault and rollback simulators.
- If you have no API key, GenAI cells run in **offline demo mode**. Offline scores show how the code works, not real model quality. (Today's notebook has no GenAI cells.)
- Never paste keys, connection strings or passwords into a notebook cell, a prompt or a chat.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day21_PostRead_Azure_Deployment_and_CD_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Review the CD pipeline cells; Azure steps run in class only (subscription window). | `Day21_Azure_Deployment_and_CD_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (deployment and secrets problems that run offline). Stretch problem optional. | `Day21_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: Azure and CD questions (Sections A to C). | `Day21_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 18: write a deployment runbook for SmartDesk. OpenAI Codex allowed; review every line. | `Day21_App_Build_Prompts.md` |

## Submit

**Runbook (one page):** deploy, verify, read logs, roll back to the previous tag, rotate a Key Vault secret, clean up.

## Stuck?

- `ModuleNotFoundError`: run the install cell again, then **Runtime > Restart session**.
- The Key Vault SDK cell says skipped: that is expected offline. Use the simulator above it.
- Not sure which tag to roll back to: print `r.history` in the release simulator and pick the last good tag.
- Did you create Azure resources in class? Check `az group list -o table` and delete yours before you sleep.

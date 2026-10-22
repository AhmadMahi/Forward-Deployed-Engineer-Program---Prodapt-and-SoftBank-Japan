# Day 17 Hotel Lab: DevOps and Cloud Fundamentals

**Total time:** 105 to 120 minutes | **Day:** Wed 18 Nov 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- If you have no API key, GenAI cells run in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Azure steps use the web portal and Azure DevOps in the browser only. Do not create paid resources tonight.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day17_PostRead_DevOps_and_Cloud_Fundamentals_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then run tests and lint, and read the pipeline YAML and explain each stage. | `Day17_DevOps_and_Cloud_Fundamentals_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (DevOps, cloud model and pipeline). Stretch set optional. | `Day17_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: CI/CD and cloud questions. | `Day17_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 15: lint, tests and pipeline YAML for SmartDesk. OpenAI Codex allowed; review every line. | `Day17_App_Build_Prompts.md` |

## Submit

Your **YAML file** (`azure-pipelines.yml`) plus a **one-paragraph explanation** of what each stage does and what the team does when it goes red.

## Stuck?

- `ruff` reports import order errors: run `ruff check --fix` and read what changed.
- `bandit` exits with an error code: that means it found issues. Read them; it is not a crash.
- `pip-audit` hangs or fails offline: it needs the internet. Skip it in Colab offline and run it in class.
- `yaml.safe_load` error: check indentation. YAML uses spaces, never tabs.

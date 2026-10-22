# Day 20 Hotel Lab: Git, CI/CD and Docker

**Total time:** 105 to 120 minutes | **Day:** Mon 23 Nov 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser for the Git and security cells. Building images needs **Docker Desktop** on your laptop.
- If you have no API key, GenAI cells run in **offline demo mode**. Offline scores show how the code works, not real model quality.
- `pip-audit` needs internet. In Colab it works as is; the offline practice cell uses a sample report.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day20_PostRead_Git_CI_CD_and_Docker_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Follow the Git and Docker cells; build an image with Docker Desktop on the laptop. | `Day20_Git_CI_CD_and_Docker_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (Git workflow, pipeline and Dockerfile). Stretch problem optional. | `Day20_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: Git and Docker questions (Sections A to C). | `Day20_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 17: Dockerfile and CI with security gates. OpenAI Codex allowed; review every line. | `Day20_App_Build_Prompts.md` |

## Submit

**Vulnerability report v2** (scan before and after fixes), using `shared/templates/Vulnerability_Report_Template.md`.

## Stuck?

- `bandit: command not found`: run the install cell again, then **Runtime > Restart session**.
- Git says `Please tell me who you are`: run the `git config user.name` and `user.email` lines.
- Docker build fails with `permission denied` on Windows: start Docker Desktop first and wait for "Engine running".
- The gate still fails after a fix: re-read the finding id. Fix the pattern; do not hide it with `# nosec`.

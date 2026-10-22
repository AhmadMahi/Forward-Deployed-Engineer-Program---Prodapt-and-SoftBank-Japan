# Day 30 Hotel Lab: LLM Security and Guardrails

**Total time:** 105 to 120 minutes | **Day:** Mon 07 Dec 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- If you have no API key, GenAI cells run in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.
- Only attack systems you own or are authorised to test. The bot in the notebook is simulated.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day30_PostRead_LLM_Security_and_Guardrails_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then run the red-team suite against the simulated bot and add two indirect-injection cases (for example in a tool result and a ticket attachment name). | `Day30_LLM_Security_and_Guardrails_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (prompt injection, guardrail and responsible AI problems). Stretch problem optional. | `Day30_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: security questions (Sections A to C). | `Day30_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 25: guardrail gateway in front of SmartDesk. OpenAI Codex allowed; review every line. | `Day30_App_Build_Prompts.md` |

## Submit

**Vulnerability report v3**, using `shared/templates/Vulnerability_Report_Template.md`: at least four findings from your red-team run, each with severity, proposed fix, fixed by (human or Codex-assisted), verified (yes or no) and evidence.

## Stuck?

- Block rate is 100% but unseen attacks are 0/5: that is the lesson. Regex rules only catch what you wrote them for. Add layers, not just patterns.
- `ExpiredSignatureError` on a fresh token: check the `ttl` is positive and your clock is correct.
- The pytest cell prints nothing: make sure `redteam_cases.json` was written by the cell above it.
- Not sure about severity: High if it leaks data or performs an action, Medium if it needs other mistakes first, Low otherwise.

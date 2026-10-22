# Days 36 to 40 Hotel Lab: Capstone evenings

**Total time:** 90 to 120 minutes each evening | **Days:** Tue 15 Dec to Fri 18 Dec 2026 | **Track:** Capstone

## Before you start

- Work in your team repo in VS Code with OpenAI Codex (program API key, approved models only). Colab is fine for notebook work.
- Every change goes through a pull request that a teammate reviews. Never push straight to `main`.
- Never paste API keys, customer data or credentials into a prompt, a notebook or `AGENTS.md`. Check your daily token usage.
- No API key? Starter notebooks run in **offline demo mode**. Offline scores show how the code works, not real model quality.

## The routine (every evening)

| # | Time | Task | Where |
|---|---|---|---|
| 1 | 15 min | Stand-up prep: what I finished today, what I will finish tomorrow, what is blocking me. | Team board |
| 2 | 45 to 60 min | Checkpoint work: one small task per pull request, built with Codex, tests run, diff reviewed by a teammate. | Team repo |
| 3 | 15 min | Update the decision log and README (setup steps, AI tool disclosure). | `docs/decision_log.md`, `README.md` |
| 4 | 10 min | Post checkpoint evidence: PR links, CI status, one screenshot or metric. | Team channel |

## Day 36 evening (Tue 15 Dec)

- Finish the design review fixes from Checkpoint 1.
- Commit `AGENTS.md` (start from `shared/templates/AGENTS_learner_template.md`).
- Write the characterisation tests for your modernisation step. They must pass against the legacy code.
- **Evidence:** architecture diagram, assumptions log, link to the characterisation test PR.

## Day 37 evening (Wed 16 Dec)

- Close the gaps from the walking skeleton demo.
- Make sure every model call writes to the token log (tokens and estimated cost, placeholder prices labelled).
- Extend the golden set towards 20 items (30 for PolicyPal).
- **Evidence:** walking skeleton screenshot, golden set size, a token log sample.

## Day 38 evening (Thu 17 Dec)

- Run bandit, pip-audit and npm audit. Log findings in `docs/vulnerability_report.md`.
- Merge the modernisation step through a reviewed PR with the characterisation tests green.
- First error analysis on the evaluation run: top three failure types.
- **Evidence:** green CI with security gates, vulnerability report draft, metrics table.

## Day 39 evening (Fri 18 Dec)

- Code freeze was 17:00 IST: only demo fixes approved by your mentor.
- Finish the OWASP Agentic security checklist and the token and cost report.
- Rehearse the 10 minute demo twice; record a backup video.
- Final check of all deliverables. They are due **Day 40, Mon 21 Dec 2026, 09:00 IST**.
- **Evidence:** links to every deliverable in the README.

## Submit

Each evening, post your checkpoint evidence in the team channel. Final deliverables are listed in `00_Capstone_Guide.pdf`, section 8.

## Stuck?

- CI red after a Codex change: revert the PR, then redo it as two smaller PRs.
- A characterisation test fails after migration: the new code changed behaviour. Fix the code, not the test, unless the change is intended and in its own labelled PR.
- Scope too big: cut to the must-haves and move the rest to the backlog. Depth beats breadth.

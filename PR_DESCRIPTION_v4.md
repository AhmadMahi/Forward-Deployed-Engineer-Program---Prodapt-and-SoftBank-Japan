# FDE Program v4: repository update

Implements the v4 brief (26 Oct to 21 Dec 2026). Branch `program-v4`, 18 commits, one or more per phase. The brief asks for one pull request per phase; the commits are grouped so the branch can be split into phase PRs if preferred.

## Checks

| Check | Result |
|---|---|
| `python tools/check_notebooks.py` (offline, `OFFLINE=1`) | 37/37 notebooks pass (31 day notebooks + 6 capstone starters) |
| `python tools/check_links.py` | 591/591 links OK |
| `python tools/build/lint_content.py` (em dashes, other AI vendors, retired model default, API keys; text inside pptx, docx and pdf too) | 0 problems |
| `bash shared/SmartDesk/run_all_tests.sh` | 30/30 step test suites pass offline |
| Quiz files | 30 files, 15 rows x 7 columns each, each names the previous training day |
| Capstone dates | 15 to 21 Dec 2026 throughout; no old dates left |
| `TODO_v4.md` files | None |

## What was created, merged, split or updated

| Day | Action | Source (archive) |
|---|---|---|
| 01, 14, 19, 24, 29 | PLACEHOLDER (README only). Day 01 also has the onboarding deck and laptop checklist | FDE team |
| 02 | MERGE | old 01 + 02 |
| 03 | CONDENSE + NEW (Codex half day, about 17 slides) | old 03 |
| 04, 09, 10, 11, 15, 17, 18, 21, 22, 27, 28, 30, 31, 32, 34 | REUSE + UPDATE | old 04, 10, 11, 12, 13, 17, 22, 19, 23, 26, 27, 28, 29, 30, 33 |
| 05, 06, 07, 08, 16, 20, 26, 33, 35 | MERGE | per brief Section 3 |
| 12, 13 | SPLIT + EXPAND | old 21 |
| 23, 25 | NEW | none |
| 36 to 40 | UPDATE + Project 06 LegacyLift | old capstone |

Shared and docs: `AGENTS.md`, `docs/` (MODEL_GUIDE, CODEX_GUIDE, ACCESS_AND_INSTALL, CHANGELOG_v4), `shared/templates/` (vulnerability report, hotel lab, learner AGENTS.md, OWASP agentic checklist), `shared/Laptop_Setup_Guide.pdf`, `shared/Codex_Setup_and_Dos_Donts.pdf`, `shared/SmartDesk/` (brief, starter, 30 steps), `shared/PatchAndModernise_Starter/`, `FDE-Mindset-Source/`, `tools/`.

v1 is preserved with `git mv` in `archive/v1-40-day/` (history kept); the old README is `archive/v1-40-day/README_v1.md`.

## Additions beyond the brief

- `tools/build/`: each technical day is generated from one spec file (`specs/dayNN.py`) in the v1 visual style. Rebuild with `python tools/build/build_day.py NN`.
- `tools/build/lint_content.py`: enforces the AGENTS.md content rules.
- Quiz answer positions rebalanced across A to D (v1 answers were almost all B). Correct answer texts are unchanged.

## Conflicts between the brief and the repo (brief followed)

1. **FDE-Mindset-Source "unchanged" vs "no other AI vendors anywhere".** The copied v1 FDE files still name other assistants in their app prompts. They are kept unchanged as instructed and excluded from the lint; noted in `FDE-Mindset-Source/README.md`.
2. **Archive "move" vs "keep intact".** FDE material and the capstone were copied (not moved) out of the archive so `archive/v1-40-day/` stays complete.
3. **Model names after the author's reference date.** GPT-6.1 Sol, GPT-6 Luna, GPT-6 Astra and the notebook default ID `gpt-6.1-sol` come from the brief and are marked "confirm against the approved model list". Override with `LLM_MODEL`.
4. **SmartDesk step README links.** The brief's relative path pattern resolved to the wrong folder; links use `../../../DayMM-...` and pass the link check.
5. **MCP SDK v2.** FastMCP is now `MCPServer` in the installed SDK (mcp 2.3.0); Day 28 and SmartDesk step 24 use the current API. The SDK has no task store, so the Tasks lifecycle is simulated in the notebook.

## Items for trainers to confirm before delivery

- Approved model list and the `LLM_MODEL` default.
- Hosted Agents API details, Codex `config.toml` / `codex mcp add` syntax and the A2A Agent Card path and signature format (Days 27 and 28 slides say to check current docs).
- OpenTelemetry GenAI attribute names (Day 35 says "check the current spec version").
- EU AI Act Art. 50 and Japan AI Guidelines v1.2 wording on Day 23 (check against current official sources).
- `shared/PatchAndModernise_Starter/TRAINER_NOTES.md` is the answer key and sits inside the starter folder. Move it before giving learners the folder on its own.
- The 50-question pre-assessment Excel file is not in the repo (Day 01 README explains where to add it).
- Branding: the materials keep the repository's existing visual style; no logo was added.

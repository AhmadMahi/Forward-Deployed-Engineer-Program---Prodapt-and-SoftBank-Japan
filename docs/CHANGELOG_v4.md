# Changelog: Program v4

Prepared 22 Oct 2026 for the delivery from Mon 26 Oct to Mon 21 Dec 2026. The previous version is kept unchanged in [archive/v1-40-day](../archive/v1-40-day/README_v1.md).

## Structure

- 15 Basics + 15 GenAI + 5 FDE Mindset + 5 Capstone days; calendar 26 Oct to 21 Dec 2026 with the Deepavali holiday on Mon 9 Nov.
- GenAI starts in Week 3 (Days 12 and 13), with at least one GenAI day every week after.
- Basics cut from 17 to 15 days: Python days combined (Day 2), OOP condensed (Day 3), FastAPI from 5 days to 3 (Days 5 to 7), Spark days merged (Day 16).
- FDE Mindset content consolidated into Days 1, 14, 19, 24 and 29, owned by the FDE team. v1 FDE material is in [FDE-Mindset-Source](../FDE-Mindset-Source/README.md).

## New content

- OpenAI Codex half day (Day 3), with [CODEX_GUIDE.md](CODEX_GUIDE.md) and [MODEL_GUIDE.md](MODEL_GUIDE.md).
- Industry use cases and an SME session on agentic security, Patching as a Service and Code Modernisation as a Service, with the Patch and Modernise assignment (Day 23).
- Small language models and token cost optimisation, with a token cost calculator notebook (Day 25).
- Persistent agent memory (Day 27).

## Updated GenAI content

Tokens and the model landscape, structured outputs, context engineering, LangChain v1, LangGraph durable execution, hosted agents, MCP 2026-07-28, A2A v1.0, OWASP Top 10 for Agentic Applications, trajectory evals, AgentOps, OpenTelemetry GenAI conventions.

## Security thread

Dependency hygiene (Day 3), OWASP API Top 10 (Day 7), vulnerability reports v1 to v3 (Days 7, 20, 30), CI security gates (Day 20), agent identity and scoped tokens (Days 23 and 30).

## Other changes

- New per-day `Hotel_Lab.md` for the evening hands-on.
- SmartDesk running project across all technical days ([shared/SmartDesk](../shared/SmartDesk/README.md)).
- Capstone moved to 15 to 21 Dec 2026, with the new Project 06 LegacyLift and v4 baseline requirements.
- OpenAI only: OpenAI Codex replaces mixed AI-assistant references; notebook default model now comes from `LLM_MODEL` (the v1 default model was replaced).
- Quizzes re-paired to the previous training day (FDE days and the holiday are skipped). Answer positions rebalanced across A to D (v1 answers were almost all B).
- New tools: `tools/check_notebooks.py`, `tools/check_links.py`, and the build scripts in `tools/build/` that generate each day's deck, PDFs, workbook and notebook from one spec file.

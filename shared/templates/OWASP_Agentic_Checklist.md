# OWASP Agentic Security Checklist (template)

NEW (v4). Used on Day 23 (SME session), Day 30 (guardrails and red-team) and in every capstone project.

**Source:** OWASP Top 10 for Agentic Applications for 2026, OWASP GenAI Security Project, 9 Dec 2025: <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026>. Related: the OWASP Agent Control Standard (Aug 2026) and Framework Crosswalk (Sep 2026) at <https://genai.owasp.org/owasp-top-10-for-agentic-applications>.

**How to use it:** this checklist groups the risks into practical themes. Before you use it, open the official list and write the matching OWASP identifier (ASI01 to ASI10) in the "OWASP ID" column. Memory poisoning is ASI06. Do not guess IDs; copy them from the source, because the list may be revised.

**Project:** ____________________ | **Reviewer:** ____________________ | **Date:** ____________

## 1. Checklist

| # | Theme | Check | OWASP ID | Status (pass, fail, n/a) | Evidence (file, test, screenshot) |
|---|---|---|---|---|---|
| 1 | Goal and instruction hijack | Untrusted text (documents, web pages, tickets, tool output) cannot change the agent's goal or rules. System rules are kept separate from data. | | | |
| 2 | Tool misuse | Every tool has a narrow purpose, validated inputs and an allow-list of actions. Destructive tools need human approval. | | | |
| 3 | Identity and privilege | The agent has its own identity. Tokens are scoped, short-lived and revocable. No long-lived keys inside prompts, code or agent config. | | | |
| 4 | Supply chain | MCP servers, skills, plugins, models and packages come from trusted sources, are pinned to versions and are reviewed before use. | | | |
| 5 | Code execution | Generated code runs only in a sandbox: container, no network by default, CPU, memory and time limits. | | | |
| 6 | Memory and context poisoning (ASI06) | Long-term memory is scoped per user, has an expiry, records its source, and can be deleted on request. Untrusted content is not written to memory without checks. | ASI06 | | |
| 7 | Agent-to-agent communication | Messages between agents are authenticated (for example signed A2A Agent Cards) and validated like any other input. | | | |
| 8 | Cascading failures | Loops have step and cost limits. Failures stop safely and do not trigger other agents without checks. | | | |
| 9 | Human trust | The UI shows when output is AI-generated, what the agent did, and asks for confirmation on high-impact actions. | | | |
| 10 | Rogue or drifting behaviour | Every action is logged and traced. Alerts fire on unusual tool use, cost spikes or policy violations. There is a kill switch. | | | |

## 2. Agent permissions table

List every tool the agent can call. Default is **deny**.

| Tool | Allowed actions | Scope (data it can touch) | Needs human approval? | Token lifetime | Owner |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |

## 3. Supply chain register

| Component (MCP server, skill, package, model) | Source | Version or hash | Reviewed by | Date | Notes |
|---|---|---|---|---|---|
| | | | | | |

## 4. Sign-off

- Open findings are logged in the vulnerability report (`shared/templates/Vulnerability_Report_Template.md`).
- Residual risks accepted by: ____________________

This checklist is a teaching aid. It does not replace a professional security review or legal advice.

# Patch and modernise: SmartDesk legacy CSV module (Day 23 SME assignment)

## Scan findings
| ID | Finding | Tool | Severity | Affected file | Proposed fix | Fixed by | Verified | Evidence |
|---|---|---|---|---|---|---|---|---|
| PM-01 | `eval()` on CSV input | bandit B307 | High | legacy/csv_import_legacy.py | Validate against an allow-list, `int()` | Codex-assisted | Yes | `test_modern_never_evals_input` |
| PM-02 | SQL built with string formatting | bandit B608 | High | legacy/csv_import_legacy.py | Parameterised queries | Codex-assisted | Yes | `test_modern_blocks_sql_injection` |
| PM-03 | Errors silently ignored | Code review | Medium | legacy/csv_import_legacy.py | Return rejected rows with line numbers | Human | Yes | `test_bad_rows_are_reported_not_hidden` |

## Approach
1. Write characterisation tests against the legacy code to capture today's behaviour.
2. Ask Codex for a modern version in small steps; run the tests after each step.
3. Keep behaviour identical for valid rows; change it on purpose only for unsafe input.
4. Swap callers to `modern.csv_import`, then delete the legacy module in a later PR.

## SmartDesk maturity level
**Pilot moving to production.** SmartDesk has tests, CI security gates, a deployed service and GenAI features with offline tests, but no evaluation gate, guardrails or monitoring yet (Days 30 to 35). What moves it to production: a golden-set quality gate, guardrails, observability and a named owner for incidents.

## What we would offer a customer as a service
- **Patching as a Service:** continuous scanning, AI-proposed patches, tests that prove each fix, human approval, rollout with an SLA (for example critical fixes in 72 hours).
- **Code Modernisation as a Service:** assess, plan (rehost to rebuild), migrate with coding agents in small verified steps, prove with characterisation tests.

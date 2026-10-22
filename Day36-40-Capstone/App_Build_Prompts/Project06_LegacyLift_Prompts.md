# Project 06: LegacyLift App Build Prompts (NEW v4)

**Project:** LegacyLift: Modernise a Legacy Order-Management App

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Run the prompts in order with OpenAI Codex in VS Code (program API key, approved models only), one per working session. Ask Codex for a plan first, then build in small steps.
2. Review every diff before you accept it. You must be able to explain all of it on demo day.
3. Commit after each prompt with a clear message, through a reviewed pull request. Keep CI green.
4. Record in your README which parts were generated and how you checked them.
5. Never paste API keys, customer data or credentials into a prompt or AGENTS.md. Check your daily token usage.

> **The rule for this project:** tests first. No line of legacy behaviour changes until a characterisation test pins it. Behaviour changes go in separate, labelled pull requests.

---

## Prompt 1: Assess, pin and plan (Day 36)

```text
You are a senior engineer leading a code modernisation for "LegacyLift" in 5 days.
Customer: Sakura Telecom Accessories, a telecom retailer in India and Japan; 40 store staff use a 12-year-old Python order desk script.
Problem: legacy_orders.py mixes data, rules and printing, uses global state and datetime.utcnow(), has no tests,
and requirements_legacy.txt pins PyYAML==5.3.1 (known vulnerability). The business needs identical totals, tax and discounts.

Use the files from our starter notebook (legacy_orders.py, requirements_legacy.txt, data/orders.json, data/snapshot.json,
test_characterisation.py). Do NOT modify legacy_orders.py.
1. Create a monorepo: legacy/ (the untouched script), api/ (FastAPI, Pydantic v2, SQLAlchemy 2.0, pytest), web/ (React, Vite),
   tests/characterisation/, eval/, ops/ (Dockerfiles, docker-compose.yml, azure-pipelines.yml), docs/.
2. Write docs/assessment.md: a module map (each function, its inputs, outputs, side effects, risks) and, per module,
   a recommended path (rehost, replatform, refactor or rebuild) with a reason.
3. Extend the characterisation tests: status transitions, rounding, shipping threshold, unknown products, discounts at 10 and 15.
   They must pass against legacy/ before any other work.
4. AGENTS.md: build and test commands, "never edit legacy/", "one function per PR", "never put secrets in prompts".
5. CI pipeline that runs the characterisation suite on every pull request.
Show me the plan first. Then the diff.
```

---

## Prompt 2: Migrate the core, one function per PR (Day 37)

```text
Migration step by step for LegacyLift. For EACH step: write or reuse the tests, make the smallest change, run the full
characterisation suite against the new code, and stop for my review before the next step.
Step 1: api/pricing.py compute_total(items, discount_pct) with no print and no global state. Same outputs.
Step 2: SQLAlchemy models (Order, OrderLine, Product) and create_order with timezone-aware dates (datetime.now(datetime.UTC)).
Step 3: set_status as an explicit state machine with the same allowed transitions.
Step 4: FastAPI endpoints: POST /orders/quote, POST /orders, PATCH /orders/{id}/status, GET /orders/{id}, GET /orders.
Add a comparison script that runs all 300 sample orders through legacy and new code and reports any difference (must be 0).
Every model call (if any) must log input, output and reasoning tokens and an estimated cost (placeholder prices, labelled).
```

---

## Prompt 3: New behaviour, front end and security (Day 38)

```text
For LegacyLift:
1. In a SEPARATE pull request labelled "behaviour change": discounts above 10% go to an approval queue
   (POST /approvals/{id}/approve by a manager role, JWT with short-lived scoped tokens). Update the tests and note the change in docs/decision_log.md.
2. React order screen: create an order, see the quote, see "pending approval" for big discounts. Loading, error and empty states.
3. Security: run bandit, pip-audit and npm audit; add them as CI gates. Remove PyYAML==5.3.1 and prove it with a re-run.
   Log every finding in docs/vulnerability_report.md (copy shared/templates/Vulnerability_Report_Template.md):
   finding, tool, severity, file, fix, fixed by human or Codex-assisted, verified, evidence.
4. Fill in docs/security_checklist.md for the OWASP Top 10 for Agentic Applications (copy shared/templates/OWASP_Agentic_Checklist.md),
   one line of evidence per item, including how Codex was sandboxed and what it could not touch.
5. AI feature: an "explain legacy function" helper or an order-notes summariser behind our API (never from the browser),
   with an offline stand-in, a golden set of at least 20 items and a quality gate that exits 1 on failure.
```

---

## Prompt 4: Deploy, observe and prepare the demo (Day 39)

```text
For LegacyLift:
1. Production Dockerfiles (small base image, non-root, health checks) and docker-compose for local runs.
2. azure-pipelines.yml: Test (characterisation + unit), Scan (bandit, pip-audit, npm audit), Evaluate (quality gate),
   Build (images), DeployDev, DeployProd with approval.
3. A strangler switch: an environment flag that routes quotes to legacy or new code, and a daily comparison report.
4. A monitoring view: requests, p95 latency, error rate, legacy-vs-new mismatches, approvals pending, tokens and estimated cost.
5. docs/token_cost_report.md: tokens and estimated cost per request and per 1,000 requests, before and after one optimisation.
   Label every price as a placeholder.
6. docs/modernisation_note.md: the steps, the PR links, what changed in behaviour and why, risks left, and what you would
   offer a customer as a "Code Modernisation as a Service" package.
7. Draft an 8 to 12 slide demo outline and a runbook for "new code gives a different total from legacy".
```

---

## Stretch ideas

- Data migration script with reconciliation counts
- Japanese and English invoice output
- A Codex skill or AGENTS.md section that documents the team's migration recipe

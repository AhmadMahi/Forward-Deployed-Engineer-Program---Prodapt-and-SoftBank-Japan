# Day 15: App Build Prompts

**App of the day:** FDE Field Notebook (FastAPI + React)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 15. A practical tool FDEs can actually use on engagements: log assumptions, decisions, status updates and blockers per customer.

---

## Prompt 1: Build the back end

```text
You are a senior full stack mentor. Build the FastAPI back end for an "FDE Field Notebook".
Python 3.11, FastAPI, Pydantic v2, SQLAlchemy 2.0, SQLite.
Entities (each belongs to an Engagement: id, customer_name, sponsor, start_date, goal):
- Assumption: text, confidence (low|medium|high), how_to_test, status (open|confirmed|disproved), checked_on
- Decision: date, decision, options_considered, rationale, door_type (one_way|two_way), agreed_by
- StatusUpdate: date, situation, action, next_step, next_date, ask
- Blocker: description, owner, raised_on, escalated (bool), resolved_on
Endpoints: CRUD for each under /api/engagements/{id}/..., plus GET /api/engagements/{id}/summary returning counts,
open assumptions, unresolved blockers older than 3 days, and the latest status update. Include TestClient tests.
```

---

## Prompt 2: Build the React front end

```text
Build a React (Vite) front end for the FDE Field Notebook:
- Engagement list and a detail page with tabs: Assumptions, Decisions, Updates, Blockers
- Forms with controlled inputs; one-way door decisions require the agreed_by field
- The status update form shows a live preview in the "situation, action, next, ask" format and a Copy button
- A summary card highlighting unresolved blockers older than 3 days in orange
Handle loading, error and empty states. Teal theme.
```

---

## Prompt 3: Make it useful in real life

```text
Suggest five small features that would make the FDE Field Notebook genuinely useful during a customer engagement
(for example, exporting a weekly update as Markdown). For the top two, give the code changes needed in the API and React app.
```

---

## Stretch ideas (try on your own)

- Export the weekly status updates as a Markdown file.
- Add a simple search across all notes for an engagement.
- Add a reminder list of assumptions not checked in the last 7 days.

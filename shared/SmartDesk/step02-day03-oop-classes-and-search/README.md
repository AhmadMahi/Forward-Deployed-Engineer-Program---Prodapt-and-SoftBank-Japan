# SmartDesk step 02 (Day 3): Ticket, Customer and Agent classes

**Increment:** Ticket, Customer and Agent classes; first Codex feature (search)

**Day folder:** [../../../Day03-OOP-and-OpenAI-Codex-Walkthrough/](../../../Day03-OOP-and-OpenAI-Codex-Walkthrough/) (see `Day03_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 01](../step01-day02-cli-ticket-logger/) | Next: [step 03](../step03-day04-mongodb-and-chart/)

## Goal

Model SmartDesk with classes and add the first OpenAI Codex feature: ticket search.

## What changed from the previous step

Replaces the dictionaries from step 01 with dataclasses, a custom exception, a subclass (`UrgentTicket`) and a `TicketStore` with `search`.

## Key files

- `models.py`: classes, custom exception and the search feature
- `test_models.py`: tests
- `codex_review_note.md`: one-line review note and tokens used for the Codex feature

## How to run

```bash
python models.py
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.

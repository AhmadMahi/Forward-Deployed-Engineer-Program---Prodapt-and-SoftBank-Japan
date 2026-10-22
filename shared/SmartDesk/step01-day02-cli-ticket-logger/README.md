# SmartDesk step 01 (Day 2): CLI ticket logger

**Increment:** CLI ticket logger with functions; tickets saved as JSON

**Day folder:** [../../../Day02-Python-Basics-Functions-and-Files/](../../../Day02-Python-Basics-Functions-and-Files/) (see `Day02_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [the starter](../starter/) | Next: [step 02](../step02-day03-oop-classes-and-search/)

## Goal

Log support tickets from the command line using functions, lists, dictionaries and a JSON file.

## What changed from the previous step

Starts from the [starter](../starter/). Adds `add_ticket`, `save_tickets`, input checks and a `stats` command.

## Key files

- `smartdesk.py`: load, add, save and count tickets
- `test_smartdesk.py`: tests for each function

## How to run

```bash
python smartdesk.py list
python smartdesk.py add "Aiko Tanaka" network high "No signal at home"
python smartdesk.py stats
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.

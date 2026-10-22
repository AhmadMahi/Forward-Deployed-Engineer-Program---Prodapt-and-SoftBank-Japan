# Build tools for day materials

Each technical day is generated from one spec file, so content stays consistent and the v1 visual style is kept.

| File | Purpose |
| --- | --- |
| `fde_render.py` | Renders a spec into the deck (.pptx), pre-read, post-read and hands-on PDFs, workbook (.docx) and Colab notebook |
| `build_day.py` | `python tools/build/build_day.py 12` (one day), `... 2 3 4` (several) or `... all` |
| `specs/dayNN.py` | The content of one day |
| `lint_content.py` | Checks for em dashes, other AI vendors, the retired v1 model default and API keys |
| `extras/` | One-off builders: shared PDFs and Day 1 deck, README generator, Day 23 one-pager, capstone files |

App build prompts, quizzes and hotel labs are plain files in each day folder and are edited by hand.

## Spec format

A spec is a Python module with these names:

- `DAY`, `FOLDER`, `SLUG`, `TITLE`, `SUBTITLE`, `DATE`, `TRACK`, `NEXT`
- `DECK`: a list of slides. Types: `cards`, `flow`, `table`, `bullets`, `bullets_code`, `code`, `compare`, `callout`, `section`. Add `new=True` to show the `NEW (v4)` tag, `note=` for a teal line under the content, `greet=` for the footer greeting. Title, connect and thank-you slides are added automatically.
- `PREREAD`, `POSTREAD`: `title`, `lede`, `sections` (each with `h`, `sub`, `paras`, `bullets`, `table`, `code`, `box`, `after`, `new`)
- `HANDSON`: `lede`, optional `how`, `problems` (each with `title`, `level`, `concepts`, `text`, `sample`, `hints`, `new`)
- `WORKBOOK`: `sections` with `kind` = `blanks`, `short`, `predict`, `code` or `reflection`
- `NOTEBOOK`: `subtitle`, `cells` as tuples: `("md", text)`, `("code", source)`, `("code", source, ["skip-offline-check"])`, `("helpers",)` for the shared GenAI helpers
- Optional `EXTRA_NOTEBOOKS`: extra notebooks for the same day (used on Day 25)

Inline `**bold**` works in every text field. See `specs/day12.py` for a complete example.

## Before you commit

```bash
python tools/build/build_day.py NN
python tools/build/lint_content.py DayNN
python tools/check_notebooks.py DayNN --skip-pip
python tools/check_links.py
```

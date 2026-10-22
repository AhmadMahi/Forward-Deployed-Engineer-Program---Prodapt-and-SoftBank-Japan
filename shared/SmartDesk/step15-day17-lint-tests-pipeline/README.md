# SmartDesk step 15 (Day 17): Lint, tests and pipeline YAML

**Increment:** Lint, tests and pipeline YAML

**Day folder:** [../../../Day17-DevOps-and-Cloud-Fundamentals/](../../../Day17-DevOps-and-Cloud-Fundamentals/) (see `Day17_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 14](../step14-day16-pyspark-sla-metrics/) | Next: [step 16](../step16-day18-rag-faq-citations/)

## Goal

Make SmartDesk ready for CI: a lint config, tests and an Azure Pipelines YAML file with a first security scan.

## What changed from the previous step

Adds `pyproject.toml` (ruff and pytest settings), `azure-pipelines.yml` with lint, bandit and test steps, and a short explanation of each stage.

## Key files

- `azure-pipelines.yml`: CI pipeline
- `pyproject.toml`: ruff and pytest config
- `PIPELINE_EXPLAINED.md`: one paragraph per stage
- `app/`: minimal service the pipeline builds

## How to run

```bash
ruff check .
bandit -r app -ll
pytest -q
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.

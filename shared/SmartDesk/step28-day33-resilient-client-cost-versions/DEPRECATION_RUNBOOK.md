# Model deprecation runbook

1. **Notice:** the provider announces a retirement date (example: GPT-5.5 left Codex on 14 Oct 2026).
2. **Inventory:** search the registry and code for the model name. List every release that uses it.
3. **Candidate:** pick the replacement from the approved model list (docs/MODEL_GUIDE.md).
4. **Evaluate:** run the golden set and the quality gate (step 27) with the candidate. Compare quality, cost and latency.
5. **Canary:** release to 10% of traffic through the gateway (step 29). Watch dashboards for a day.
6. **Switch and record:** move to 100%, create a new release entry, add the old model to `RETIRED_MODELS`.

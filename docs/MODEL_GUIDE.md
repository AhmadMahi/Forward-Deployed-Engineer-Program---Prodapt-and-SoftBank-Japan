# OpenAI Model Guide

Used on Day 3 (OpenAI Codex walkthrough) and Day 25 (token cost and optimisation), and by every GenAI notebook.

> Model names were checked on 21 Oct 2026. Confirm them against the program's approved model list for the API key before each delivery. Names and availability change often.

## Which model for which task

| Task | Model | Reasoning effort | Why |
|---|---|---|---|
| Explain code, small edits, docstrings, simple tests | Lighter cost-efficient model (for example GPT-6 Luna, if on the approved list) | Low | Cheapest tokens for routine work. |
| Most feature work: endpoints, components, refactors across a few files | Default Codex model: GPT-6.1 Sol | Medium | OpenAI's recommended default for most Codex tasks (Oct 2026); balanced cost and quality. |
| Hard debugging, design decisions, large migrations | GPT-6.1 Sol at higher reasoning effort; top-tier GPT-6 Astra only with trainer approval | High | Higher effort and top-tier models cost more per task; use them only when the default fails. |
| Security scan review and patch proposals | Default model (GPT-6.1 Sol), with human verification of every fix | Medium | Patches must be tested; the model proposes, the engineer decides. |
| Retired or legacy models (for example GPT-5.5) | Do not use | n/a | GPT-5.5 retired from Codex for ChatGPT sign-ins on 14 Oct 2026; migrate to the current default. |

## Notebook default

- Every GenAI notebook reads the model name from the `LLM_MODEL` environment variable.
- The default in `genai_helpers.py` is `gpt-6.1-sol`. This identifier must be confirmed against the approved model list before class. If it differs, set `LLM_MODEL` (Colab Secrets or `.env`) rather than editing every notebook.
- The v1 notebook default model has been replaced in every v4 notebook.
- Without an `OPENAI_API_KEY`, or with `OFFLINE=1`, notebooks run in offline demo mode. Offline results show how the code works, not real model quality.

## OpenAI Codex: do's and don'ts

**Do**

- Plan first for multi-step work; approve the plan, then let Codex build in small steps.
- Keep tasks small and include only the relevant files to save tokens.
- Write or generate tests first; run them after every change.
- Read every diff; accept only code you can explain.
- Keep AGENTS.md updated with build, test and style rules.
- Use workspace-write sandbox with approvals; read-only for exploration.
- Run bandit, pip-audit and npm audit on AI-generated code; log findings.
- Check your daily token usage; stop runaway tasks.

**Don't**

- Paste API keys, customer data or credentials into prompts or AGENTS.md.
- Use full-access or bypass modes on any laptop with real credentials.
- Ask open-ended 'improve everything' requests or paste the whole codebase.
- Use a top-tier model or high reasoning effort for routine edits.
- Merge AI code without tests and a human review.
- Use models outside the program's approved list.

## Prices

The program does not publish real prices in course material. Every notebook uses placeholder prices, labelled `PLACEHOLDER`. Replace them with the approved price sheet when you need real numbers.

## Sources

- S03: ChatGPT and Codex changelog (GPT-5.5 retires from Codex, 14 Oct 2026). https://learn.chatgpt.com/docs/changelog
- S33: OpenAI upgrading ChatGPT and Codex with GPT-6 Sol and GPT-6 Luna, 9to5Mac, 22 Sep 2026. https://9to5mac.com/2026/09/22/openai-upgrading-chatgpt-and-codex-with-two-more-gpt-6-models/
- S34: OpenAI Fast and Ultrafast mode (GPT-6 Astra, GPT-6.1 Sol via API), LiteLLM docs, 6 Oct 2026. https://docs.litellm.ai/docs/providers/openai/ultrafast

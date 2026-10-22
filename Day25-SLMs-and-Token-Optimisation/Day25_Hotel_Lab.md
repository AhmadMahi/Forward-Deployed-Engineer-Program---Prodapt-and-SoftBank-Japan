# Day 25 Hotel Lab: SLMs and Token Optimisation

**Total time:** 90 to 105 minutes | **Day:** Mon 30 Nov 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. For the small model, choose **Runtime > Change runtime type > GPU**. Free GPU availability varies; without one, the notebook falls back to a smaller model on CPU.
- No API key or no model download? Every cell runs in **offline demo mode** with a labelled stand-in. Offline scores show how the code works, not real model quality.
- Every price in both notebooks is a **placeholder**. Label it as one in anything you submit.
- Some small models need a free Hugging Face account. Never paste tokens or keys into a notebook cell.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the SLM and token cost post-read. | `Day25_PostRead_SLMs_and_Token_Optimisation_Recap_and_Beyond.pdf` |
| 2 | 40 min | Open the notebook in Colab (GPU runtime; CPU fallback with a smaller model). Run a small open-weight model on the 20 SmartDesk tickets and compare accuracy and latency with the OpenAI API model. | `Day25_SLMs_and_Token_Optimisation_Colab.ipynb` |
| 3 | 30 min | Estimate SmartDesk cost per 1,000 tickets. Apply caching, trimming and model routing, and record the saving. | `Day25_Token_Cost_Calculator_Colab.ipynb` |
| 4 | 10 min | Submit (see below). | |

Optional, if you have time: hands-on problems in `Day25_HandsOn_Problem_Statements.pdf`, the workbook `Day25_Workbook_Interactive.docx`, and SmartDesk step 21 in `Day25_App_Build_Prompts.md` (OpenAI Codex allowed; review every line).

## Submit

1. **SLM vs LLM comparison table:** model, accuracy, average latency, estimated cost per 1,000 tickets, and the tickets each got wrong.
2. **Cost report:** cost per 1,000 tickets before and after caching, trimming and routing, with the saving in percent. State that prices are placeholders.

## Stuck?

- `CUDA out of memory`: restart the runtime and use the CPU fallback model.
- Model download fails or asks for a login: the notebook switches to the offline stand-in. Note this in your table.
- Routing saves nothing: check the escalation rate. If most tickets escalate, lower the threshold or improve the classifier prompt.
- Numbers look tiny: they are per request. Multiply by tickets per day.

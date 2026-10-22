"""Cost per 1,000 tickets before and after optimisation. All prices are PLACEHOLDERS."""
from token_cost import cost

BASE = {"system": 900, "context": 1500, "ticket": 120, "output": 250}      # tokens per request, all-LLM design


def per_1000(input_t, output_t, cached_t=0, llm_share=1.0):
    return round(1000 * llm_share * cost(input_t, output_t, cached_t), 4)


def report(slm_share=0.75):
    inp = BASE["system"] + BASE["context"] + BASE["ticket"]
    rows = [("Baseline: LLM for every ticket", per_1000(inp, BASE["output"]))]
    rows.append(("+ prompt caching (stable system prompt)", per_1000(inp, BASE["output"], cached_t=BASE["system"])))
    trimmed = BASE["system"] + 500 + BASE["ticket"]                            # top-k 2 instead of 6 chunks
    rows.append(("+ context trimming (top-k 2)", per_1000(trimmed, BASE["output"], cached_t=BASE["system"])))
    rows.append(("+ output limit (120 tokens)", per_1000(trimmed, 120, cached_t=BASE["system"])))
    rows.append((f"+ routing: SLM handles {int(slm_share * 100)}%", per_1000(trimmed, 120, BASE["system"], 1 - slm_share)))
    return rows


if __name__ == "__main__":
    for name, value in report():
        print(f"{name:<44} {value:>8.4f} per 1,000 tickets (placeholder prices)")

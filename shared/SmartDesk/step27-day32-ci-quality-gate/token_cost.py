"""Token cost helpers. Prices are PLACEHOLDERS, not real prices. Replace them with the approved price sheet."""

PRICE_PER_1M = {"input": 1.00, "cached_input": 0.10, "output": 4.00}   # PLACEHOLDER prices per 1M tokens


def cost(input_t, output_t, cached_t=0, reasoning_t=0, prices=PRICE_PER_1M):
    """Estimated cost of one request. Reasoning tokens are billed as output."""
    fresh = input_t - cached_t
    return (fresh * prices["input"] + cached_t * prices["cached_input"]
            + (output_t + reasoning_t) * prices["output"]) / 1_000_000

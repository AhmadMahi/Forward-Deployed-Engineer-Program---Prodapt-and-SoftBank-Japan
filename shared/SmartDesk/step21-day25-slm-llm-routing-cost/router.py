"""SmartDesk step 21: SLM first for classification, escalate to the LLM when the SLM is unsure.

Offline the SLM is a keyword model with a confidence score. On Day 25 you swap in a small open-weight model
run with Hugging Face Transformers (SLM_BACKEND=hf) and compare accuracy, latency and cost.
"""
import os
import time

from llm_client import complete

KEYWORDS = {"billing": ["bill", "charge", "refund", "invoice", "payment", "roaming"],
            "network": ["signal", "network", "slow", "5g", "4g", "call", "router", "data"],
            "account": ["password", "login", "log in", "account", "sim", "email", "code"]}


def slm_classify(text):
    """Return (label, confidence)."""
    if os.getenv("SLM_BACKEND") == "hf":
        from transformers import pipeline                  # Day 25 notebook: GPU runtime, CPU fallback
        clf = pipeline("zero-shot-classification", model=os.getenv("SLM_MODEL", "typeform/distilbert-base-uncased-mnli"))
        r = clf(text, candidate_labels=list(KEYWORDS) + ["other"])
        return r["labels"][0], float(r["scores"][0])
    low = text.lower()
    hits = {c: sum(w in low for w in ws) for c, ws in KEYWORDS.items()}
    total = sum(hits.values())
    if total == 0:
        return "other", 0.4
    best = max(hits, key=hits.get)
    return best, round(hits[best] / total, 2)


def llm_classify(text):
    out, usage = complete(f"Classify as billing, network, account or other. Reply with one word.\n{text}",
                          max_tokens=5)
    label = out.strip().lower()
    return (label if label in list(KEYWORDS) + ["other"] else slm_classify(text)[0]), usage


def route(text, threshold=0.7):
    t0 = time.perf_counter()
    label, conf = slm_classify(text)
    if conf >= threshold:
        return {"label": label, "by": "slm", "confidence": conf, "usage": {"input_tokens": 0, "output_tokens": 0},
                "ms": round((time.perf_counter() - t0) * 1000, 2)}
    label, usage = llm_classify(text)
    return {"label": label, "by": "llm", "confidence": conf, "usage": usage,
            "ms": round((time.perf_counter() - t0) * 1000, 2)}

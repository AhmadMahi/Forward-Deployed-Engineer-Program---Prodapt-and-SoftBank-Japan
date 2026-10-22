"""SmartDesk step 12: category classification with structured output and prompt templates."""
import json
from typing import Literal

from pydantic import BaseModel, ValidationError

from llm_client import complete, is_online
from prompts import CLASSIFY_SYSTEM, CLASSIFY_USER, SCHEMA

KEYWORDS = {"billing": ["bill", "charge", "refund", "invoice", "payment", "roaming"],
            "network": ["signal", "network", "slow", "5g", "4g", "call", "router", "data"],
            "account": ["password", "login", "log in", "account", "sim", "email", "code"]}


class Classification(BaseModel):
    category: Literal["billing", "network", "account", "other"]
    priority: Literal["low", "medium", "high"]
    reason: str


def offline_classify(body):
    low = body.lower()
    scores = {c: sum(w in low for w in ws) for c, ws in KEYWORDS.items()}
    best = max(scores, key=scores.get)
    category = best if scores[best] else "other"
    urgent = any(w in low for w in ["no signal", "twice", "doubled", "blocked", "cannot", "today"])
    priority = "high" if urgent else "low" if "?" in body else "medium"
    return {"category": category, "priority": priority, "reason": "offline keyword rules"}


def classify(body):
    """Return a validated Classification. Falls back to 'other' if the model output is invalid."""
    if is_online():
        text, _ = complete(CLASSIFY_USER.substitute(body=body), system=CLASSIFY_SYSTEM, json_schema=SCHEMA)
        raw = json.loads(text)
    else:
        raw = offline_classify(body)
    try:
        return Classification(**raw)
    except ValidationError:
        return Classification(category="other", priority="medium", reason="invalid model output")

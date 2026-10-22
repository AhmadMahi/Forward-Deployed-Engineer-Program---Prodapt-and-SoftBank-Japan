"""SmartDesk step 11: ticket summary with token logging."""
import csv
import os
from datetime import date, datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from llm_client import MODEL, complete
from token_cost import cost

app = FastAPI(title="SmartDesk summariser", version="0.11.0")
LOG = os.getenv("TOKEN_LOG", "token_log.csv")
FIELDS = ["timestamp", "ticket_id", "model", "input_tokens", "output_tokens", "est_cost"]


class Ticket(BaseModel):
    id: int
    body: str = Field(min_length=1, max_length=4000)


def log_usage(ticket_id, usage):
    row = {"timestamp": datetime.now().isoformat(timespec="seconds"), "ticket_id": ticket_id, "model": MODEL,
           **usage, "est_cost": round(cost(usage["input_tokens"], usage["output_tokens"]), 6)}
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)
    return row


@app.post("/summarise")
def summarise(t: Ticket):
    try:
        text, usage = complete(f"Summarise this telecom support ticket in one line:\n{t.body}")
    except Exception as e:
        raise HTTPException(503, f"LLM unavailable: {type(e).__name__}")
    log_usage(t.id, usage)
    return {"summary": text, "usage": usage}


@app.get("/usage/today")
def usage_today():
    if not os.path.exists(LOG):
        return {"calls": 0, "tokens": 0, "est_cost": 0.0}
    with open(LOG) as f:
        rows = [r for r in csv.DictReader(f) if r["timestamp"].startswith(date.today().isoformat())]
    return {"calls": len(rows), "tokens": sum(int(r["input_tokens"]) + int(r["output_tokens"]) for r in rows),
            "est_cost": round(sum(float(r["est_cost"]) for r in rows), 6), "note": "placeholder prices"}

"""Write Day36-40-Capstone/Starter_Notebooks/Project06_LegacyLift_Starter.ipynb (NEW in v4)."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
OUT = os.path.join(ROOT, "Day36-40-Capstone", "Starter_Notebooks", "Project06_LegacyLift_Starter.ipynb")
SIGN = ("Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)")

CELLS = [
    ("md", f"""# Project 06: LegacyLift Starter (NEW v4)
**LegacyLift: Modernise a Legacy Order-Management App**

{SIGN}

---
This notebook writes the customer's legacy order module, generates sample orders, pins the legacy behaviour with
characterisation tests, and gives you a target FastAPI skeleton that must match the legacy outputs. Then you migrate
one function at a time with OpenAI Codex, tests first.

* **Option A (Google Colab)** cells are active; **Option B (VS Code)** lines are commented. Toggle with `Ctrl + /`.
* No API key is needed. The optional AI cell runs in offline demo mode without one."""),
    ("md", "## 1. Setup"),
    ("code", """# ===== Option A: Google Colab (active) =====
!pip install -q fastapi httpx pytest bandit pip-audit

# ===== Option B: VS Code / local =====
# pip install fastapi httpx pytest bandit pip-audit
# Optional key for the AI cell: a git-ignored .env file with OPENAI_API_KEY=...
import os, sys
sys.path.insert(0, os.getcwd())
print("Setup done")"""),
    ("md", """## 2. The legacy module
This is what Sakura Telecom Accessories runs today. **Do not edit it.** It mixes data, rules and printing, keeps
global state, uses a deprecated date API (`datetime.utcnow()`), and its requirements pin a library version with a
known vulnerability."""),
    ("code", '''%%writefile legacy_orders.py
# legacy_orders.py: order desk script, written in 2014. Do not edit; migrate it.
import datetime

ORDERS = {}                     # global state
NEXT_ID = [1000]
PRICES = {"CASE-01": 1200.0, "CHG-20W": 1500.0, "CBL-USB": 450.0, "SIM-5G": 300.0, "EAR-BT": 2500.0}
GST = 0.18


def compute_total(items, discount_pct=0):
    sub = 0
    for code, qty in items:
        if code not in PRICES:
            raise KeyError("unknown product " + code)
        sub = sub + PRICES[code] * qty
    if discount_pct > 10:
        print("DISCOUNT NEEDS APPROVAL")          # old behaviour: prints and ignores the discount
        discount_pct = 0
    sub = sub * (1 - discount_pct / 100.0)
    if sub < 3000:
        shipping = 99
    else:
        shipping = 0
    return round(sub * (1 + GST) + shipping, 2)


def create_order(store, items, discount_pct=0):
    oid = "ORD-" + str(NEXT_ID[0])
    NEXT_ID[0] = NEXT_ID[0] + 1
    ORDERS[oid] = {"id": oid, "store": store, "items": items, "discount": discount_pct,
                   "total": compute_total(items, discount_pct), "status": "NEW",
                   "created": datetime.datetime.utcnow().isoformat()}      # deprecated API
    print("created", oid)
    return oid


def set_status(oid, status):
    o = ORDERS[oid]
    allowed = {"NEW": ["PAID", "CANCELLED"], "PAID": ["SHIPPED"], "SHIPPED": [], "CANCELLED": []}
    if status not in allowed[o["status"]]:
        return False
    o["status"] = status
    return True'''),
    ("code", '''%%writefile requirements_legacy.txt
PyYAML==5.3.1'''),
    ("md", "PyYAML 5.3.1 is pinned on purpose: versions before 5.4 have a known arbitrary code execution vulnerability "
           "(CVE-2020-14343). Your scans must find it and your migration must remove it."),
    ("md", "## 3. Sample data: 300 orders"),
    ("code", '''import json, random
import legacy_orders as L

random.seed(606)
codes = list(L.PRICES)
orders = []
for i in range(300):
    items = [(random.choice(codes), random.randint(1, 4)) for _ in range(random.randint(1, 3))]
    discount = random.choice([0, 0, 0, 5, 10, 15])
    orders.append({"store": random.choice(["BLR-01", "BLR-02", "TKY-01", "OSA-01"]), "items": items,
                   "discount": discount})
os.makedirs("data", exist_ok=True)
json.dump(orders, open("data/orders.json", "w"), indent=1)
print(len(orders), "orders written. Example:", orders[0])'''),
    ("md", """## 4. Characterisation tests (write these BEFORE any change)
Characterisation tests describe what the code **does today**, including odd behaviour. They are your safety net.
Run them against the legacy code now, and against your new code after every migration step."""),
    ("code", '''%%writefile test_characterisation.py
import importlib
import json

import pytest

TARGET = "legacy_orders"          # later: point this at your new module, e.g. "order_service"


@pytest.fixture
def m():
    return importlib.import_module(TARGET)


def test_golden_example(m):
    assert m.compute_total([("CASE-01", 3)]) == 4248.00            # 3 x 1,200 + 18% GST, free shipping


def test_small_order_pays_shipping(m):
    assert m.compute_total([("SIM-5G", 1)]) == round(300 * 1.18 + 99, 2)


def test_ten_percent_discount_applied(m):
    assert m.compute_total([("EAR-BT", 2)], 10) == round(2500 * 2 * 0.9 * 1.18, 2)


def test_big_discount_not_applied(m):
    assert m.compute_total([("EAR-BT", 2)], 15) == m.compute_total([("EAR-BT", 2)], 0)


def test_unknown_product_rejected(m):
    with pytest.raises(KeyError):
        m.compute_total([("NOPE", 1)])


def test_snapshot_of_300_orders(m):
    snap = json.load(open("data/snapshot.json"))
    orders = json.load(open("data/orders.json"))
    got = [m.compute_total([tuple(i) for i in o["items"]], o["discount"]) for o in orders]
    assert got == snap'''),
    ("code", '''# Record the legacy outputs once (the "golden master"), then run the tests.
import contextlib, io, pytest
with contextlib.redirect_stdout(io.StringIO()):          # the legacy code prints; keep the output tidy
    snap = [L.compute_total([tuple(i) for i in o["items"]], o["discount"]) for o in orders]
json.dump(snap, open("data/snapshot.json", "w"))
code = pytest.main(["-q", "-p", "no:cacheprovider", "test_characterisation.py"])
assert code == 0, "Characterisation tests must pass against the legacy code"
print("All characterisation tests pass against the legacy code.")'''),
    ("md", """## 5. Target: a FastAPI skeleton (strangler pattern)
The new service starts as a thin wrapper that **delegates to the legacy code**, so behaviour is identical from day one.
Then you replace one function at a time with clean, typed code, keeping the characterisation tests green."""),
    ("code", '''%%writefile order_service.py
"""New order service. Step 0: delegate to legacy. Replace one function per pull request."""
from pydantic import BaseModel, Field

import legacy_orders as legacy

APPROVAL_LIMIT = 10          # discounts above this go to the approval queue (NEW behaviour, in its own PR)


class Line(BaseModel):
    code: str
    qty: int = Field(gt=0, le=100)


class Quote(BaseModel):
    store: str
    items: list[Line]
    discount_pct: float = Field(default=0, ge=0, le=50)


def compute_total(items, discount_pct=0):
    # TODO (migration step 1): reimplement without the print and without global state; keep the tests green.
    return legacy.compute_total(items, discount_pct)'''),
    ("code", '''import importlib
import order_service
importlib.reload(order_service)
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI(title="LegacyLift order service")
APPROVAL_QUEUE = []


@app.post("/orders/quote")
def quote(q: order_service.Quote):
    items = [(line.code, line.qty) for line in q.items]
    if q.discount_pct > order_service.APPROVAL_LIMIT:
        APPROVAL_QUEUE.append(q.model_dump())
        return {"status": "pending_approval", "total_without_discount": order_service.compute_total(items, 0)}
    try:
        return {"status": "ok", "total": order_service.compute_total(items, q.discount_pct)}
    except KeyError as e:
        raise HTTPException(status_code=422, detail=str(e))


api = TestClient(app)
print(api.post("/orders/quote", json={"store": "TKY-01", "items": [{"code": "CASE-01", "qty": 3}]}).json())
print(api.post("/orders/quote", json={"store": "TKY-01", "items": [{"code": "EAR-BT", "qty": 1}],
                                      "discount_pct": 15}).json())
print(api.post("/orders/quote", json={"store": "TKY-01", "items": [{"code": "NOPE", "qty": 1}]}).status_code)'''),
    ("code", '''# Run the same characterisation suite against the NEW module.
src = open("test_characterisation.py").read().replace('TARGET = "legacy_orders"', 'TARGET = "order_service"')
open("test_characterisation_new.py", "w").write(src)
with contextlib.redirect_stdout(io.StringIO()):
    code = pytest.main(["-q", "-p", "no:cacheprovider", "test_characterisation_new.py"])
assert code == 0
print("New module matches legacy behaviour on all characterisation tests.")'''),
    ("md", """## 6. Security scan before you start
Record every finding in `docs/vulnerability_report.md` (template: `shared/templates/Vulnerability_Report_Template.md`).
pip-audit needs network access; in offline mode it is skipped and you note that in the report."""),
    ("code", '''import subprocess
r = subprocess.run([sys.executable, "-m", "bandit", "-q", "legacy_orders.py"], capture_output=True, text=True)
print("bandit:", (r.stdout or r.stderr or "no findings").strip()[:600])
if os.getenv("OFFLINE") == "1":
    print("pip-audit: skipped in offline mode. Run: pip-audit -r requirements_legacy.txt")
else:
    r = subprocess.run([sys.executable, "-m", "pip_audit", "-r", "requirements_legacy.txt"], capture_output=True,
                       text=True, timeout=180)
    print("pip-audit:", (r.stdout or r.stderr).strip()[:600])'''),
    ("md", """## 7. Optional AI feature: explain a legacy function (offline safe)
A migration assistant that explains legacy code, with token logging. Without a key it uses an offline stand-in.
Model from `LLM_MODEL`; confirm the default against the approved model list in `docs/MODEL_GUIDE.md`."""),
    ("code", '''import inspect

def _key():
    if os.getenv("OFFLINE") == "1":
        return None
    try:
        from google.colab import userdata
        return userdata.get("OPENAI_API_KEY")
    except Exception:
        return os.getenv("OPENAI_API_KEY")

KEY = _key()
MODEL = os.getenv("LLM_MODEL", "gpt-6.1-sol")       # confirm against the approved model list
PRICE_PER_1M = {"input": 1.00, "output": 4.00}      # PLACEHOLDER prices, not real

def explain(fn):
    src = inspect.getsource(fn)
    prompt = f"Explain what this legacy function does, list its side effects and risks, in 5 bullets:\\n{src}"
    if KEY:
        from openai import OpenAI
        r = OpenAI(api_key=KEY).chat.completions.create(model=MODEL, messages=[{"role": "user", "content": prompt}])
        text, tin, tout = r.choices[0].message.content, r.usage.prompt_tokens, r.usage.completion_tokens
    else:
        side = [w for w in ("print", "global", "utcnow", "ORDERS", "NEXT_ID") if w in src]
        text = f"[offline demo] {fn.__name__}: side effects or risks found: {', '.join(side) or 'none'}"
        tin, tout = max(1, len(prompt) // 4), max(1, len(text) // 4)
    cost = (tin * PRICE_PER_1M["input"] + tout * PRICE_PER_1M["output"]) / 1_000_000
    print(text)
    print(f"tokens in={tin} out={tout} est_cost={cost:.6f} (placeholder prices)")

explain(L.create_order)'''),
    ("md", "## 8. Golden set seed"),
    ("code", '''golden = [{"id": "ll-001", "input": {"items": [["CASE-01", 3]], "discount": 0}, "expect": 4248.00},
          {"id": "ll-002", "input": {"items": [["EAR-BT", 1]], "discount": 15}, "expect": "pending_approval"},
          {"id": "ll-003", "input": {"items": [["NOPE", 1]], "discount": 0}, "expect": "422 unknown product"}]
with open("data/golden_seed.jsonl", "w") as f:
    for g in golden:
        f.write(json.dumps(g) + "\\n")
print("Seeded", len(golden), "golden items. Extend to at least 20.")'''),
    ("md", """## 9. Your migration plan
1. Commit the legacy code, data and characterisation tests. CI runs them on every PR.
2. Migration step 1: `compute_total` without print or global state (one PR).
3. Step 2: `create_order` with SQLAlchemy and timezone-aware dates (`datetime.now(datetime.UTC)`).
4. Step 3: `set_status` as a validated state machine.
5. Step 4: remove `PyYAML==5.3.1`; re-run pip-audit; update the vulnerability report.
6. Behaviour changes (approval queue, negative quantities) go in **separate, labelled PRs**.

---
**Ganbatte** (頑張って): *Do your best*

""" + SIGN),
]


def main():
    cells = []
    for kind, src in CELLS:
        c = {"cell_type": "markdown" if kind == "md" else "code", "metadata": {}, "source": src}
        if kind == "code":
            c.update(execution_count=None, outputs=[])
        cells.append(c)
    nb = {"cells": cells, "metadata": {"colab": {"provenance": []},
                                        "kernelspec": {"name": "python3", "display_name": "Python 3"},
                                        "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 0}
    json.dump(nb, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("Wrote", OUT)


if __name__ == "__main__":
    main()

"""Update the v1 capstone prompts and starter notebooks for v4 (run once, after copying from the archive).

- Day numbers remapped to the v4 calendar.
- OpenAI Codex as the AI coding tool; SupportPilot "Copilot" renamed "Assistant".
- v4 baseline (AGENTS.md, modernisation step, OWASP Agentic checklist, vulnerability report, token and cost report).
- Starter notebooks: OFFLINE=1 override, LLM_MODEL default from docs/MODEL_GUIDE.md, a modernisation step cell.
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)
import capstone_content as C  # noqa: E402

CAP = os.path.join(ROOT, "Day36-40-Capstone")
OLD_TO_NEW = {13: 15, 14: 16, 16: 16, 18: 20, 22: 18, 23: 22, 25: 26, 26: 27, 27: 28, 28: 30, 29: 31, 30: 32,
              32: 33, 34: 35, 35: 35}
DAYREF = re.compile(r"\bDays? (\d+)((?:(?:, | and )\d+)*)")


def remap(text):
    def sub(m):
        nums = [int(n) for n in re.findall(r"\d+", m.group(0))]
        if any(n > 35 for n in nums):
            return m.group(0)
        new = []
        for n in nums:
            v = OLD_TO_NEW.get(n, n)
            if v not in new:
                new.append(v)
        if len(new) == 1:
            return f"Day {new[0]}"
        return "Days " + ", ".join(str(n) for n in new)
    return DAYREF.sub(sub, text)


HOW_TO = """## How to use these prompts

1. Run the prompts in order with OpenAI Codex in VS Code (program API key, approved models only), one per working session. Ask Codex for a plan first, then build in small steps.
2. Review every diff before you accept it. You must be able to explain all of it on demo day.
3. Commit after each prompt with a clear message, through a reviewed pull request. Keep CI green.
4. Record in your README which parts were generated and how you checked them.
5. Never paste API keys, customer data or credentials into a prompt or AGENTS.md. Check your daily token usage.
"""

V4_PROMPT1 = """NEW (v4) baseline for every project:
- AGENTS.md at the repo root: build, test and style commands, folders not to touch, "never put secrets in prompts".
- Modernisation step: {modern}
- docs/security_checklist.md mapped to the OWASP Top 10 for Agentic Applications (copy shared/templates/OWASP_Agentic_Checklist.md).
- docs/vulnerability_report.md (copy shared/templates/Vulnerability_Report_Template.md).
- Every model call logs input, output and reasoning tokens and an estimated cost (placeholder prices, labelled).
"""

V4_PROMPT3 = """4. NEW (v4): Run bandit, pip-audit and npm audit; add them as CI gates. Log every finding in docs/vulnerability_report.md
   (finding, tool, severity, file, fix, fixed by human or Codex-assisted, verified, evidence). Fill in docs/security_checklist.md
   for the OWASP Top 10 for Agentic Applications with one line of evidence per item.
5. NEW (v4): Finish the modernisation step: characterisation tests green before and after, one reviewed PR per step.
"""

V4_PROMPT4 = """6. NEW (v4): Write docs/token_cost_report.md: tokens and estimated cost per request and per 1,000 requests from the token log,
   then apply one optimisation (prompt caching layout, context trimming, smaller model or routing) and show before and after.
   Label every price as a placeholder.
"""


def update_prompts():
    for p in C.PROJECTS[:5]:
        path = os.path.join(CAP, "App_Build_Prompts", f"{p['file']}_Prompts.md")
        s = open(path, encoding="utf-8").read()
        s = re.sub(r"## How to use these prompts\n\n(?:\d\..*\n)+", HOW_TO, s)
        s = s.replace("Agentic Customer Support Copilot", "Agentic Customer Support Assistant")
        s = s.replace("The team wants a copilot", "The team wants an assistant")
        s = s.replace("the copilot", "the assistant")
        s = remap(s)
        s = s.replace("Include a README skeleton and an AGENTS.md with commands and conventions.\n```",
                      "Include a README skeleton and an AGENTS.md with commands and conventions.\n"
                      + V4_PROMPT1.format(modern=p["modern"]) + "```")
        s = re.sub(r"(   script that exits with code 1 when thresholds fail\. Add it to the CI pipeline\.\n)",
                   lambda m: m.group(1) + V4_PROMPT3, s)
        s = s.replace("5. Write a runbook for the most likely production incident.\n",
                      "5. Write a runbook for the most likely production incident.\n" + V4_PROMPT4)
        assert "NEW (v4)" in s and s.count("NEW (v4)") >= 4, path
        open(path, "w", encoding="utf-8").write(s)


LEGACY = {
    "ShopSmart": '''# Legacy code to modernise (do not edit it; pin its behaviour first)
_INDEX = []                                   # hidden global state

def legacy_search(query, products):
    """Exact-word keyword search from the old site. Case-sensitive, no ranking."""
    global _INDEX
    _INDEX = products
    words = query.split()
    return [p["id"] for p in _INDEX if all(w in p["name"] or w in p["description"] for w in words)]

sample = [{"id": "P1", "name": "Aoi kettle", "description": "A quiet kettle for small apartments."},
          {"id": "P2", "name": "Mori lamp", "description": "A modern lamp."}]

# Characterisation tests: they describe what the code DOES today, including odd behaviour.
assert legacy_search("quiet kettle", sample) == ["P1"]
assert legacy_search("Kettle", sample) == []          # case-sensitive today
assert legacy_search("", sample) == ["P1", "P2"]      # empty query returns everything today
print("Characterisation tests pass. Now migrate behind the same interface, one verified step at a time.")''',
    "BookFinder": '''# Legacy code to modernise (do not edit it; pin its behaviour first)
import sqlite3

def legacy_import(rows, conn):
    """Old CSV import: builds SQL strings by hand (injection risk) and skips rows silently."""
    conn.execute("CREATE TABLE IF NOT EXISTS books (id TEXT, title TEXT, year INT)")
    n = 0
    for r in rows:
        if not r.get("title"):
            continue
        conn.execute("INSERT INTO books VALUES ('%s', '%s', %d)" % (r["id"], r["title"].replace("'", "''"), int(r["year"])))
        n += 1
    return n

conn = sqlite3.connect(":memory:")
rows = [{"id": "B1", "title": "Kyoto Mystery", "year": 2019}, {"id": "B2", "title": "", "year": 2020},
        {"id": "B3", "title": "Ronin's Path", "year": 2015}]
# Characterisation tests
assert legacy_import(rows, conn) == 2
assert conn.execute("SELECT title FROM books WHERE id='B3'").fetchone()[0] == "Ronin's Path"
print("Characterisation tests pass. Migrate to SQLAlchemy models with parameterised writes.")''',
    "PolicyPal": '''# Legacy code to modernise (do not edit it; pin its behaviour first)
def legacy_faq_answer(question):
    """Old help desk bot: keyword if/else, no citations."""
    q = question.lower()
    if "leave" in q and "carry" in q:
        return "Up to 10 days can be carried forward."
    if "vpn" in q:
        return "Use the company VPN on all public networks."
    return "Please contact the help desk."

# Characterisation tests: keep the refusal behaviour when you replace this with RAG.
assert legacy_faq_answer("Can I carry forward my leave?").startswith("Up to 10 days")
assert legacy_faq_answer("Is there a company gym?") == "Please contact the help desk."
print("Characterisation tests pass. Replace with the RAG service behind the same function signature.")''',
    "SupportPilot": '''# Legacy code to modernise (do not edit it; pin its behaviour first)
REFUNDS_TODAY = 0.0                            # hidden global state

def legacy_refund(amount, days_late):
    """Old refund script: procedural, global state, no validation."""
    global REFUNDS_TODAY
    pct = min(0.05 * days_late, 0.5)
    refund = round(amount * pct, 2)
    REFUNDS_TODAY += refund
    return refund

# Characterisation tests
assert legacy_refund(1000, 3) == 150.0
assert legacy_refund(1000, 20) == 500.0        # capped at 50%
assert legacy_refund(1000, -2) == -100.0       # bug today: negative days give a negative refund. Fix in a separate, labelled PR.
print("Characterisation tests pass. Turn this into the validated calculate_refund tool.")''',
    "InsightDesk": '''# Legacy code to modernise (do not edit it; pin its behaviour first)
REPORT = []                                    # hidden global state, grows on every run

def legacy_daily_report(sales, date):
    """Old pandas-style report: appends to a global list, so re-runs duplicate rows."""
    for s in sales:
        if s["date"] == date:
            REPORT.append({"store": s["store"], "revenue": s["qty"] * s["price"]})
    return sum(r["revenue"] for r in REPORT if True)

sales = [{"date": "2026-11-15", "store": "TKY-01", "qty": 2, "price": 500},
         {"date": "2026-11-15", "store": "BLR-02", "qty": 1, "price": 900}]
# Characterisation tests
assert legacy_daily_report(sales, "2026-11-15") == 1900
assert legacy_daily_report(sales, "2026-11-15") == 3800   # bug today: not idempotent
REPORT.clear()
print("Characterisation tests pass. Migrate to an idempotent gold table job with reconciliation.")''',
}


def update_notebooks():
    for p in C.PROJECTS[:5]:
        path = os.path.join(CAP, "Starter_Notebooks", f"{p['file']}_Starter.ipynb")
        nb = json.load(open(path, encoding="utf-8"))
        for c in nb["cells"]:
            src = "".join(c["source"]) if isinstance(c["source"], list) else c["source"]
            src = src.replace('def _get_key():\n    try:',
                              'def _get_key():\n    if os.getenv("OFFLINE") == "1":                 '
                              '# force offline demo mode (used by tools/check_notebooks.py)\n        return None\n    try:')
            src = src.replace('MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")                 '
                              '# change to any current chat model you have access to',
                              '# Default model: confirm against the approved model list (docs/MODEL_GUIDE.md). '
                              'Override with LLM_MODEL.\nMODEL = os.getenv("LLM_MODEL", "gpt-6.1-sol")')
            src = src.replace("OPENAI_API_KEY=sk-...", "OPENAI_API_KEY=... (git-ignored .env file)")
            src = src.replace("Agentic Customer Support Copilot", "Agentic Customer Support Assistant")
            src = src.replace("Baseline copilot", "Baseline assistant")
            src = src.replace("copilot", "assistant")
            if c["cell_type"] == "markdown":
                src = remap(src)
            c["source"] = src
        assert "gpt-4o-mini" not in json.dumps(nb), path
        # insert the modernisation step before the closing sign-off cell
        new_cells = [
            {"cell_type": "markdown", "metadata": {}, "source":
                "## NEW (v4): Modernisation step\nEvery capstone project includes one modernisation step. Below is a "
                "small legacy function from the customer's old system. Run the characterisation tests, then migrate it "
                "with OpenAI Codex in small, verified pull requests. Keep these tests green before and after each step."},
            {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
             "source": LEGACY[p["key"]]},
        ]
        if not any("Modernisation step" in "".join(c["source"]) for c in nb["cells"]):
            nb["cells"][-1:-1] = new_cells
        json.dump(nb, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    update_prompts()
    update_notebooks()
    print("Prompts and starter notebooks updated.")

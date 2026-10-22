"""SmartDesk step 26: evaluate the RAG assistant on a golden set and build a small dashboard.

Offline metrics are simple and explainable. Online you can add an LLM judge, calibrated against human labels.
"""
import json
from collections import defaultdict
from pathlib import Path

from rag import FaqRag
from retrieval import tokens

HERE = Path(__file__).parent


def load_golden(path=HERE / "golden_set.jsonl"):
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]


def faithfulness(answer, context):
    """Share of answer words (minus the citation) that appear in the retrieved context."""
    words = [w for w in tokens(answer) if not w.startswith("faq")]
    ctx = set(tokens(context))
    return round(sum(w in ctx for w in words) / len(words), 2) if words else 0.0


def relevance(answer, question):
    q = set(tokens(question))
    return round(len(q & set(tokens(answer))) / len(q), 2) if q else 0.0


def evaluate(rag=None, golden=None):
    rag, golden = rag or FaqRag(), golden or load_golden()
    rows = []
    for g in golden:
        hits = rag.retrieve(g["question"])
        out = rag.answer(g["question"])
        context = " ".join(d["text"] for _, d in hits)
        expected = g["source"]
        rows.append({"id": g["id"], "category": g["category"],
                     "retrieval_hit": (expected in [d["id"] for _, d in hits]) if expected else not out["citations"],
                     "citation_ok": (out["citations"] == [expected]) if expected else out["citations"] == [],
                     "contains_fact": all(m.lower() in out["answer"].lower() for m in g["must_include"]),
                     "faithfulness": faithfulness(out["answer"], context) if expected else 1.0,
                     "relevance": relevance(out["answer"], g["question"])})
    return rows


def summary(rows, by=None):
    groups = defaultdict(list)
    for r in rows:
        groups[r[by] if by else "all"].append(r)
    keys = ["retrieval_hit", "citation_ok", "contains_fact", "faithfulness", "relevance"]
    return {g: {k: round(sum(float(r[k]) for r in rs) / len(rs), 2) for k in keys} | {"n": len(rs)}
            for g, rs in groups.items()}


def trajectory_pass_k(trajectories, expected_tools, k):
    """pass^k: the agent is right only if all k runs of the same task use the expected tool sequence."""
    runs = trajectories[:k]
    return len(runs) == k and all(r == expected_tools for r in runs)


def dashboard(rows, path=HERE / "eval_dashboard.md"):
    lines = ["# SmartDesk evaluation dashboard", "", "| Slice | n | Retrieval hit | Citation OK | Contains fact | Faithfulness | Relevance |",
             "|---|---|---|---|---|---|---|"]
    for name, s in {**summary(rows), **summary(rows, "category")}.items():
        lines.append(f"| {name} | {s['n']} | {s['retrieval_hit']} | {s['citation_ok']} | {s['contains_fact']} | "
                     f"{s['faithfulness']} | {s['relevance']} |")
    failures = [r["id"] for r in rows if not (r["retrieval_hit"] and r["contains_fact"])]
    lines += ["", f"Failures to analyse: {', '.join(failures) or 'none'}",
              "", "Offline scores show how the code works, not real model quality."]
    Path(path).write_text("\n".join(lines) + "\n")
    return path


if __name__ == "__main__":
    rows = evaluate()
    print(json.dumps(summary(rows, "category"), indent=2))
    print("Dashboard:", dashboard(rows))

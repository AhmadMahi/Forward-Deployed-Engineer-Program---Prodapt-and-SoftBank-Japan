"""AgentOps registry: version prompts, tools, skills, MCP servers and models together.

A release is the set of versions that was evaluated together. Retired models block a release.
"""
import hashlib

RETIRED_MODELS = {"gpt-5.5"}        # GPT-5.5 left Codex on 14 Oct 2026; check the approved list
RELEASES = {
    "2026.12.1": {"model": "gpt-6.1-sol", "prompt": "summarise-v3", "tools": "ticket-tools-1.2",
                  "mcp_server": "smartdesk-tickets-0.24.0", "skill": "refund-policy-2"},
}
PROMPTS = {"summarise-v3": "Summarise this telecom support ticket in one line. Be neutral. No promises."}


def prompt_hash(name):
    return hashlib.sha256(PROMPTS[name].encode()).hexdigest()[:12]


def check_release(release):
    problems = []
    if release["model"] in RETIRED_MODELS:
        problems.append(f"model {release['model']} is retired: follow the deprecation runbook")
    if release["prompt"] not in PROMPTS:
        problems.append(f"prompt {release['prompt']} not in the registry")
    return problems


def cost_by_version(log):
    """log rows: release, model, input_tokens, output_tokens, est_cost. Returns totals per release and model."""
    totals = {}
    for r in log:
        key = (r["release"], r["model"])
        t = totals.setdefault(key, {"calls": 0, "tokens": 0, "est_cost": 0.0})
        t["calls"] += 1
        t["tokens"] += r["input_tokens"] + r["output_tokens"]
        t["est_cost"] = round(t["est_cost"] + r["est_cost"], 6)
    return totals

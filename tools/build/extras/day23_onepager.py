"""Build Day23_Industry_Use_Cases_OnePager.pdf (NEW (v4)).

Usage: python tools/build/extras/day23_onepager.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.dirname(HERE))
import fde_render as R  # noqa: E402

OUT = os.path.join(ROOT, "Day23-Industry-Use-Cases-and-Agentic-Security-SME", "Day23_Industry_Use_Cases_OnePager.pdf")

SECTIONS = [
    dict(h="GenAI use cases by industry", table=[
        ["Industry", "Good first use cases", "Main risks"],
        ["Telecom", "Care assistant over approved FAQs; ticket triage; incident summaries",
         "Customer data; wrong outage or billing information"],
        ["BFSI", "Form and claim extraction; compliance search", "Regulation; explainability; data residency"],
        ["Retail", "Product content; semantic search; support chat", "Brand tone; wrong prices"],
        ["Healthcare", "Clinical note drafts for review; patient FAQs", "Patient safety; privacy"],
        ["Manufacturing", "Maintenance manual search; quality reports", "Unsafe instructions; IP"],
    ]),
    dict(h="Maturity levels", table=[
        ["Level", "To reach the next level"],
        ["Experiment: demo, no real users", "A real problem, a sponsor, a baseline metric"],
        ["Pilot: small group of real users", "Measured win, owner, evals, security review"],
        ["Production: SLAs and monitoring", "Shared platform, cost controls, reuse"],
        ["Scaled: many teams", "Guardrails and approvals for agent actions"],
        ["Agentic: agents act with tools", "Continuous evals, red-teaming, audit"],
    ]),
    dict(h="Do's and don'ts", table=[
        ["Do", "Don't"],
        ["Use only data you are allowed to use; minimise personal data", "Paste customer data or secrets into prompts"],
        ["Keep a human in the loop for money, safety and rights", "Let an agent act on high-impact decisions alone"],
        ["Tell people when they deal with AI; label AI content", "Hide AI-generated content or decisions"],
    ], after=["**Transparency:** EU AI Act Art. 50 (tell people they deal with AI; mark AI content) and Japan AI "
              "Business Guidelines v1.2 (voluntary, risk-based). Check current official sources. Not legal advice."]),
]


def main():
    st = R._pdf_styles()
    flow = []
    R._header(flow, st, "DAY 23 | ONE-PAGER", "Industry Use Cases and Maturity",
              "NEW (v4). A quick reference for Session 1. Examples are illustrative, not customer results.")
    R._render_blocks(flow, SECTIONS, st)
    R._doc(OUT, "Day 23  |  Industry use cases one-pager", "Day 23  |  Industry use cases one-pager", flow)
    print("wrote", os.path.relpath(OUT, ROOT))


if __name__ == "__main__":
    main()

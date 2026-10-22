"""Input and output guardrails for SmartDesk. Simple, explainable rules; a model-based classifier can be added online."""
import re

INJECTION = [r"ignore (all |any )?(previous|prior|above) instructions", r"disregard (the|your) (rules|instructions)",
             r"you are now", r"reveal (the|your) (system prompt|instructions)", r"developer mode", r"pretend to be",
             r"<\s*/?\s*system\s*>", r"act as (an? )?(admin|administrator|root)"]
INJECTION_RX = re.compile("|".join(INJECTION), re.I)
PII = {"email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "card": re.compile(r"\b(?:\d[ -]?){13,16}\b"),
       "phone": re.compile(r"\b0\d{1,3}-?\d{2,4}-?\d{3,4}\b")}
SECRET_RX = re.compile(r"(sk-[A-Za-z0-9_-]{16,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)")
PROMISES = re.compile(r"(?i)(guarantee(d)? (a )?refund|we will refund everything|legal advice)")
MAX_CHARS = 2000


def redact(text):
    for name, rx in PII.items():
        text = rx.sub(f"[{name} redacted]", text)
    return text


def check_input(text, source="user"):
    """Return (allowed, reason, cleaned_text). source is 'user' or 'document' (indirect injection path)."""
    if len(text) > MAX_CHARS:
        return False, "too long", ""
    if INJECTION_RX.search(text):
        return False, f"prompt injection ({source})", ""
    return True, "ok", redact(text)


def check_output(text):
    if SECRET_RX.search(text):
        return False, "secret in output", "Sorry, I can't share that."
    if PROMISES.search(text):
        return False, "unapproved promise", "A team lead will confirm the next steps with you."
    return True, "ok", redact(text)

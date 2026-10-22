"""Long-term memory of customer preferences, scoped per user, with expiry and deletion.

Uses the LangGraph store interface (InMemoryStore here; a database-backed store in production).
Defends against memory poisoning (OWASP ASI06): only allow-listed preference types are stored,
and text that looks like an instruction is rejected.
"""
import re
import time

from langgraph.store.memory import InMemoryStore

ALLOWED = {"channel": re.compile(r"(?i)\b(by|via|prefer)\s+(sms|email|phone|call)"),
           "language": re.compile(r"(?i)\b(in|speak)\s+(japanese|english|hindi)")}
INSTRUCTION = re.compile(r"(?i)(ignore|always approve|system prompt|you must|admin|refund everything|disregard)")
TTL_SECONDS = 90 * 24 * 3600


class PreferenceMemory:
    def __init__(self, store=None, ttl=TTL_SECONDS):
        self.store, self.ttl = store or InMemoryStore(), ttl

    def extract_and_save(self, user_id, message, consent=True):
        if not consent or INSTRUCTION.search(message):
            return []
        saved = []
        for key, rx in ALLOWED.items():
            m = rx.search(message)
            if m:
                value = m.group(2).lower().replace("call", "phone")
                self.store.put(("users", user_id, "preferences"), key, {"value": value, "expires_at": time.time() + self.ttl})
                saved.append((key, value))
        return saved

    def recall(self, user_id):
        now, out = time.time(), {}
        for item in self.store.search(("users", user_id, "preferences")):
            if item.value["expires_at"] > now:
                out[item.key] = item.value["value"]
            else:
                self.store.delete(("users", user_id, "preferences"), item.key)
        return out

    def forget(self, user_id):
        """Delete everything we remember about a user (right to deletion)."""
        for item in self.store.search(("users", user_id, "preferences")):
            self.store.delete(("users", user_id, "preferences"), item.key)

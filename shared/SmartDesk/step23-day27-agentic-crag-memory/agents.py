"""SmartDesk step 23: supervisor + corrective RAG (CRAG) + long-term memory."""
from llm_client import complete
from memory import PreferenceMemory
from retrieval import VectorIndex, load_faq, tokens

SYNONYMS = {"bars": "signal", "cut": "drop", "two": "twice", "abroad": "roaming", "wifi": "router", "code": "sms"}


class CragFaq:
    """Retrieve, grade the evidence, rewrite the query once if weak, else escalate to a human."""

    def __init__(self, threshold=0.2):
        self.docs = load_faq()
        self.index = VectorIndex([f"{d['title']}. {d['text']}" for d in self.docs])
        self.threshold = threshold

    def _best(self, q):
        s = self.index.query(q)
        i = int(s.argmax())
        return float(s[i]), self.docs[i]

    def answer(self, question):
        trace = []
        score, doc = self._best(question)
        trace.append(("retrieve", round(score, 2)))
        if score < self.threshold:
            rewritten = " ".join(SYNONYMS.get(w, w) for w in tokens(question))
            score, doc = self._best(rewritten)
            trace.append(("rewrite", rewritten, round(score, 2)))
        if score < self.threshold:
            return {"answer": "Escalated to a human agent.", "source": None, "trace": trace}
        return {"answer": f"{doc['text']} [{doc['id']}]", "source": doc["id"], "trace": trace}


class Supervisor:
    """Routes each message to a worker. Single-agent by default; workers only where they add value."""

    def __init__(self, memory=None):
        self.faq, self.memory = CragFaq(), memory or PreferenceMemory()

    def handle(self, user_id, message):
        self.memory.extract_and_save(user_id, message)
        prefs = self.memory.recall(user_id)
        low = message.lower()
        worker = "billing" if any(w in low for w in ("bill", "charge", "refund")) else "faq"
        result = self.faq.answer(message)
        reply, _ = complete(f"Reply to the customer using: {result['answer']}. Preferences: {prefs}")
        return {"worker": worker, "preferences": prefs, "reply": reply, **result}

"""Small retrieval helpers shared by the RAG steps.

Online: OpenAI embeddings. Offline: TF-IDF vectors (same interface, lower quality).
"""
import json
import os
import re
from pathlib import Path

import numpy as np

FAQ_PATH = Path(__file__).resolve().parents[1] / "data" / "telecom_faq.json"
WORD = re.compile(r"[a-z0-9]+")
STOP = {"the", "a", "an", "is", "are", "my", "i", "to", "of", "in", "on", "for", "and", "or", "it", "do", "does",
        "how", "what", "why", "can", "you", "your", "me", "after", "with", "be", "at", "this", "that", "not", "if"}


def tokens(text):
    out = []
    for w in WORD.findall(text.lower()):
        if w in STOP:
            continue
        out.append(w[:-1] if w.endswith("s") and len(w) > 4 else w)
    return out


def load_faq(path=FAQ_PATH):
    docs = json.loads(Path(path).read_text(encoding="utf-8"))
    for d in docs:
        d.setdefault("audience", "public")
    return docs


class VectorIndex:
    def __init__(self, texts):
        self.online = os.getenv("OFFLINE") != "1" and bool(os.getenv("OPENAI_API_KEY"))
        if self.online:
            from openai import OpenAI
            self.client = OpenAI()
            self.matrix = self._embed(texts)
        else:
            from sklearn.feature_extraction.text import TfidfVectorizer
            self.vec = TfidfVectorizer(tokenizer=tokens, token_pattern=None, ngram_range=(1, 2), sublinear_tf=True)
            self.matrix = self.vec.fit_transform(texts).toarray()
        n = np.linalg.norm(self.matrix, axis=1, keepdims=True)
        self.matrix = self.matrix / np.where(n == 0, 1, n)

    def _embed(self, texts):
        model = os.getenv("EMBED_MODEL", "text-embedding-3-small")
        return np.array([d.embedding for d in self.client.embeddings.create(model=model, input=texts).data])

    def query(self, text):
        q = self._embed([text]) if self.online else self.vec.transform([text]).toarray()
        q = q / (np.linalg.norm(q) or 1)
        return (self.matrix @ q.ravel())          # cosine similarity per document

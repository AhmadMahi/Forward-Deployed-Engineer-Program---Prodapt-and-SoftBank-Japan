"""SmartDesk step 19: keyword (BM25) + vector search, fused with RRF, then re-ranked."""
import math
from collections import Counter

from retrieval import VectorIndex, load_faq, tokens


class BM25:
    def __init__(self, texts, k1=1.5, b=0.75):
        self.docs = [tokens(t) for t in texts]
        self.avg = sum(map(len, self.docs)) / len(self.docs)
        self.df = Counter(w for d in self.docs for w in set(d))
        self.n, self.k1, self.b = len(self.docs), k1, b

    def scores(self, query):
        out = []
        for d in self.docs:
            tf = Counter(d)
            s = 0.0
            for w in tokens(query):
                if w in tf:
                    idf = math.log(1 + (self.n - self.df[w] + 0.5) / (self.df[w] + 0.5))
                    s += idf * tf[w] * (self.k1 + 1) / (tf[w] + self.k1 * (1 - self.b + self.b * len(d) / self.avg))
            out.append(s)
        return out


def rrf(rankings, k=60):
    """Reciprocal rank fusion of several ranked lists of document indexes."""
    fused = Counter()
    for ranking in rankings:
        for rank, idx in enumerate(ranking):
            fused[idx] += 1 / (k + rank + 1)
    return [i for i, _ in fused.most_common()]


class HybridSearch:
    def __init__(self, docs=None):
        self.docs = docs or load_faq()
        texts = [f"{d['title']}. {d['text']}" for d in self.docs]
        self.bm25, self.vec = BM25(texts), VectorIndex(texts)

    def keyword(self, q, k=5):
        s = self.bm25.scores(q)
        return sorted(range(len(s)), key=lambda i: -s[i])[:k]

    def vector(self, q, k=5):
        s = self.vec.query(q)
        return sorted(range(len(s)), key=lambda i: -s[i])[:k]

    def hybrid(self, q, k=5):
        return rrf([self.keyword(q, 10), self.vector(q, 10)])[:k]

    def rerank(self, q, candidates):
        """Cheap re-ranker: title match counts double. Swap in an LLM or cross-encoder online."""
        qt = set(tokens(q))

        def score(i):
            d = self.docs[i]
            return 2 * len(qt & set(tokens(d["title"]))) + len(qt & set(tokens(d["text"])))
        return sorted(candidates, key=lambda i: -score(i))

    def search(self, q, k=3):
        return [self.docs[i]["id"] for i in self.rerank(q, self.hybrid(q, 8))[:k]]


EVAL = [("refund for a data pack", "FAQ-01"), ("charged two times", "FAQ-02"), ("costs when travelling abroad", "FAQ-03"),
        ("when is my bill due", "FAQ-04"), ("phone shows no service bars", "FAQ-05"), ("internet slow at the station", "FAQ-06"),
        ("calls cut off on the train", "FAQ-08"), ("router red light", "FAQ-09"), ("forgot my password", "FAQ-10"),
        ("sms verification code missing", "FAQ-13")]


def hit_rate(search_fn, k=3):
    return sum(expected in search_fn(q)[:k] for q, expected in EVAL) / len(EVAL)


if __name__ == "__main__":
    h = HybridSearch()
    ids = lambda f: (lambda q: [h.docs[i]["id"] for i in f(q)])
    print("keyword :", hit_rate(ids(h.keyword)))
    print("vector  :", hit_rate(ids(h.vector)))
    print("hybrid  :", hit_rate(ids(h.hybrid)))
    print("reranked:", hit_rate(h.search))

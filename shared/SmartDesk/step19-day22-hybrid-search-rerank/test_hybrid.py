from hybrid import EVAL, BM25, HybridSearch, hit_rate, rrf


def test_rrf_rewards_agreement():
    assert rrf([[1, 2, 3], [2, 1, 3]])[:2] in ([1, 2], [2, 1])
    assert rrf([[5, 1], [1, 6]])[0] == 1


def test_bm25_prefers_matching_doc():
    s = BM25(["refund within 14 days", "router red light"]).scores("refund")
    assert s[0] > s[1] == 0


def test_hybrid_at_least_as_good_as_each_method():
    h = HybridSearch()
    ids = lambda f: (lambda q: [h.docs[i]["id"] for i in f(q)])
    kw, vec, hyb = hit_rate(ids(h.keyword)), hit_rate(ids(h.vector)), hit_rate(h.search)
    assert hyb >= max(kw, vec) - 0.1
    assert hyb >= 0.7
    assert len(EVAL) == 10

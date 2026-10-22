"""Day 22 spec. GenAI 4: Embeddings, Vector DBs and the RAG Application.
Source: archive/v1-40-day/Day23. NEW (v4) topics are marked.
"""
DAY = 22
FOLDER = "Day22-Embeddings-Vector-DBs-and-RAG-App"
SLUG = "Embeddings_Vector_DBs_and_RAG_App"
TITLE = "Embeddings, Vector DBs and the RAG App"
SUBTITLE = "Embeddings, cosine similarity, ANN indexes, hybrid search, re-ranking, and choosing RAG, fine-tuning, long context or caching"
DATE = "Wed 25 Nov 2026"
TRACK = "GenAI"
NEXT = "See you tomorrow for Day 23: industry use cases and security for the agentic world (SME session)."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 21"),
        ("Senior FDE interaction", "1 to 2 hrs: lessons from real deployments"),
        ("Embeddings (2 hrs)", "Meaning as numbers; cosine similarity"),
        ("Vector DBs (1.5 hrs)", "ANN, HNSW, IVF, metadata filters"),
        ("RAG app (2 hrs)", "Hybrid search, re-ranking, citations"),
        ("Choose the approach", "RAG, fine-tuning, long context, caching. NEW (v4)"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Use embeddings", "Embed text and compare it with cosine similarity and distance."),
        ("Pick a vector store", "Explain flat, HNSW and IVF indexes, metadata filters and trade-offs."),
        ("Combine search methods", "Fuse BM25 and vector results with RRF, then re-rank."),
        ("Choose the right approach", "Decide between RAG, fine-tuning, long context and caching by size, freshness and token cost."),
    ]),
    dict(type="callout", title="Senior FDE interaction", text="A senior Forward Deployed Engineer shares how retrieval projects really go at customers: what worked, what failed, what they would do differently.",
         sub="Come with one question about search quality or cost. Notes go in today's workbook.",
         greet="Senpai (先輩): A senior colleague who guides you"),

    dict(type="section", title="Embeddings", sub="Session 1 (2 hrs). Meaning as coordinates"),
    dict(type="cards", title="What an embedding is", greet="Imi (意味): Meaning",
         lead="\"How many leave days do I get?\" lands near \"Employees receive 18 days of paid leave\".", items=[
        ("A vector", "Text becomes a list of hundreds or thousands of numbers."),
        ("Meaning as distance", "Similar meaning means nearby vectors, even with different words."),
        ("One model, one space", "Compare only vectors made by the same embedding model."),
    ]),
    dict(type="bullets_code", title="Cosine similarity and distance", bullets=[
        "Similarity: the angle between two vectors",
        "1 means same direction, 0 unrelated",
        "Distance = 1 - similarity",
        "With unit vectors it is just a dot product",
    ], code='''import numpy as np

def cosine(a, b):
    return a @ b / (np.linalg.norm(a)
                    * np.linalg.norm(b))

q = embed("How much paid leave?")[0]
docs = embed(chunk_texts)
scores = docs @ q            # unit vectors
dist = 1 - scores            # cosine distance
best = np.argsort(scores)[::-1][:3]'''),
    dict(type="cards", title="Choosing an embedding model", items=[
        ("Languages", "Japanese and Indian languages matter here. Test on your own text."),
        ("Dimensions", "More dimensions cost more storage and memory."),
        ("Price and privacy", "API models cost per token; open-weight models can run on-prem."),
        ("Re-index on change", "New model or new chunking means re-embedding everything."),
    ]),

    dict(type="section", title="Vector databases", sub="Session 2 (1.5 hrs). Search millions of vectors in milliseconds"),
    dict(type="table", title="What a vector database adds", header=["Feature", "Why it matters"], rows=[
        ["Indexes for fast search", "No need to compare against every vector"],
        ["Metadata storage", "Keep doc name, section, date, permissions with each vector"],
        ["Filters", "\"Only public FAQ entries for Japan\""],
        ["Updates and deletes", "Keep the index in sync with changing documents"],
        ["Scale and persistence", "Millions of vectors, saved to disk, served to many users"],
    ], note="Options include FAISS (library), Chroma, pgvector, Qdrant and Azure AI Search."),
    dict(type="table", title="Exact and approximate search", header=["Index", "How it works", "Trade-off"], rows=[
        ["Flat (exact)", "Compares the query with every vector", "Perfect recall, slow at scale"],
        ["HNSW (graph)", "Hops through a graph of near neighbours", "Very fast, more memory; tune efSearch"],
        ["IVF (clusters)", "Searches only the closest clusters", "Fast, less memory; tune nprobe"],
    ], note="ANN gives up a little recall for a lot of speed. Measure recall against flat search."),
    dict(type="bullets_code", title="FAISS in practice", greet="Hayai (速い): Fast", bullets=[
        "IndexFlatIP: exact inner product",
        "IndexHNSWFlat: fast approximate graph",
        "IndexIVFFlat: clusters, needs training",
        "Measure recall of ANN against exact",
    ], code='''import faiss
d = vecs.shape[1]

flat = faiss.IndexFlatIP(d); flat.add(vecs)

hnsw = faiss.IndexHNSWFlat(d, 32,
           faiss.METRIC_INNER_PRODUCT)
hnsw.add(vecs)

ivf = faiss.IndexIVFFlat(flat, d, 64,
           faiss.METRIC_INNER_PRODUCT)
ivf.train(vecs); ivf.add(vecs)
ivf.nprobe = 8      # clusters to search'''),
    dict(type="bullets_code", title="Metadata filters", bullets=[
        "Store metadata with every vector",
        "Filter by section, date or audience",
        "Permissions are filters too (Day 18)",
        "Filter first, then rank",
    ], code='''results = collection.query(
    query_embeddings=[q],
    n_results=5,
    where={"audience": "public",
           "section": "Roaming"})'''),

    dict(type="section", title="Hybrid search and the RAG app", sub="Session 3 (2 hrs). Keywords and meaning, then the best evidence first"),
    dict(type="compare", title="Keyword and semantic search", left=dict(title="Keyword (BM25)", bullets=[
        "Exact terms: plan codes, error codes, names", "No model needed", "Misses synonyms",
    ]), right=dict(title="Semantic (vectors)", bullets=[
        "Understands paraphrases and synonyms", "Can miss rare exact terms", "Needs an embedding model",
    ])),
    dict(type="bullets_code", title="Reciprocal rank fusion (RRF)", bullets=[
        "Each method returns a ranked list",
        "Score = sum of 1 / (k + rank)",
        "Items high in both lists win",
        "No need to calibrate raw scores",
    ], code='''def rrf(rankings, k=60):
    s = {}
    for ranking in rankings:
        for r, d in enumerate(ranking, 1):
            s[d] = s.get(d, 0) + 1 / (k + r)
    return sorted(s, key=s.get, reverse=True)

final = rrf([bm25_ids, vector_ids])'''),
    dict(type="flow", title="A production retrieval pipeline", items=[
        ("Retrieve wide", "Top 20 to 50 from hybrid search"),
        ("Re-rank", "Cross-encoder or LLM scores each pair"),
        ("Keep best", "Top 3 to 5 chunks"),
        ("Generate", "Grounded prompt with citations"),
        ("Check", "Supported? Else \"I don't know\""),
    ]),
    dict(type="table", title="Re-ranker options", header=["Option", "How", "Trade-off"], rows=[
        ["Cross-encoder", "Reads query and chunk together, outputs a score", "Accurate, needs a model, slower than vectors"],
        ["LLM as re-ranker", "Ask the model to score relevance 0 to 10", "Flexible, costs tokens"],
        ["Hosted re-rank APIs", "Send query and candidates, get scores", "Easy, external dependency"],
    ]),
    dict(type="cards", title="Measure, do not guess", items=[
        ("Test set", "Ten questions with the expected chunk id, plus unanswerable ones."),
        ("hit@k", "Share of questions where the right chunk is in the top k."),
        ("MRR", "Mean of 1 / rank of the right chunk. Rewards ranking it first."),
        ("Refusals", "Unanswerable questions should get \"I don't know\"."),
    ]),

    dict(type="section", title="RAG, fine-tuning, long context or caching?", sub="Decide by size, freshness and token cost", new=True),
    dict(type="table", title="Four ways to give a model knowledge", new=True,
         header=["Approach", "Best when", "Watch out for"], rows=[
        ["RAG", "Large or changing knowledge; citations and permissions needed", "Retrieval quality is the bottleneck"],
        ["Fine-tuning", "Teach style, format or a narrow behaviour", "Bad for fast-changing facts; retrain to update"],
        ["Long context", "Small corpus that fits the window; few queries", "Every call pays for every token; quality can drop"],
        ["Prompt caching", "Large stable prefix reused by many requests", "Saves on repeated input only; prefix must match"],
    ], note="They combine: RAG for facts, caching for the stable system prompt, fine-tuning for tone."),
    dict(type="flow", title="A simple decision path", new=True, items=[
        ("Facts or style?", "Style or format: consider fine-tuning"),
        ("Fits the window?", "No: RAG"),
        ("Changes often?", "Yes: RAG, re-index on change"),
        ("Many queries?", "Yes: RAG or long context + cache"),
        ("Need citations?", "Yes: RAG"),
    ]),
    dict(type="code", title="Token cost: long context vs RAG vs caching", new=True, code='''# PLACEHOLDER prices per 1M tokens. Not real prices.
IN, CACHED, OUT = 1.00, 0.10, 4.00
corpus, rag_ctx, q, out, n = 80_000, 1_500, 50, 200, 5_000

long_ctx = n * ((corpus + q) * IN + out * OUT) / 1e6
cached   = n * (corpus * CACHED + q * IN + out * OUT) / 1e6
rag      = n * ((rag_ctx + q) * IN + out * OUT) / 1e6

print(long_ctx, cached, rag)   # 404.25  44.25  11.75''',
         note="Placeholder units. Real caching rules (minimum prefix, lifetime) vary by provider; check the docs."),
    dict(type="cards", title="SmartDesk step 19: hybrid search and re-ranking", items=[
        ("Hybrid", "BM25 + vectors with RRF over the telecom FAQ."),
        ("Re-rank", "Top 8 candidates, keep the best 3."),
        ("Measure", "hit@3 for keyword, vector, hybrid and hybrid + re-rank."),
        ("Build with Codex", "Use Day22_App_Build_Prompts.md. Review every diff."),
    ]),
    dict(type="cards", title="Key takeaways", items=[
        ("Embeddings", "Meaning as vectors; compare with cosine similarity."),
        ("Vector DBs", "Flat, HNSW, IVF; metadata filters; measure recall."),
        ("Hybrid + re-rank", "BM25 + vectors with RRF; best chunks first; cite or say \"I don't know\"."),
        ("Choose wisely", "RAG, fine-tuning, long context, caching: size, freshness, token cost."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day22_Hotel_Lab.md: compare search methods on ten questions."),
        ("Workbook", "Complete the Day 22 workbook."),
        ("Pre-read", "Read the Day 23 pre-read on industry use cases and agentic security."),
    ]),
]

PREREAD = dict(title="Searching by Meaning", lede="A light read before Day 22. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "On Day 18 you saw that an AI assistant needs the right passages from your documents. Today you learn how "
        "computers find passages by meaning, not just by matching words, how to make that search fast and accurate, and "
        "when a different approach is cheaper."]),
    dict(h="1. Meaning as a location", paras=[
        "Imagine a giant map where every sentence has a location, and sentences with similar meanings are placed close "
        "together. \"How many holidays do I get?\" sits right next to \"Employees receive 18 days of paid leave\", even "
        "though they share almost no words. The location of a sentence on this map is its **embedding**."]),
    dict(h="2. A library for these locations", paras=[
        "A **vector database** stores millions of these locations and finds the nearest ones to a question in "
        "milliseconds. Like a librarian who knows the shelves well, it does not check every book; it goes straight to "
        "the right area. This shortcut is called **approximate nearest neighbour** search."]),
    dict(h="3. Two kinds of search, better together", table=[
        ["Search type", "Strength", "Weakness"],
        ["Keyword search", "Exact terms like error code VPN-417 or a plan name", "Misses different wording for the same idea"],
        ["Meaning search", "Understands paraphrases and synonyms", "Can miss rare exact codes"]],
        paras=["Combining both is called **hybrid search**, and it is what most serious systems use."]),
    dict(h="4. A second opinion", paras=[
        "Search returns a shortlist. A **re-ranker** then reads each candidate carefully against the question and "
        "reorders them, like a hiring manager reviewing the shortlist a recruiter sent."],
        box="**Key idea:** good answers come from good evidence. Most RAG problems are search problems."),
    dict(h="5. Four ways to teach a model", new=True, paras=[
        "You can hand the model the right pages (**RAG**), retrain it on examples (**fine-tuning**), paste everything into "
        "one long message (**long context**), or let the provider remember a long opening you send every time "
        "(**caching**). Each has a different cost. Tomorrow you learn how to choose by size, freshness and token cost."]),
    dict(h="6. Think about these before class", bullets=[
        "Think of a time a search engine misunderstood you. Was it a keyword or a meaning problem?",
        "Which exact codes or plan names in telecom would keyword search handle better?",
        "If an FAQ changes every week, would you retrain a model or update a document? Why?"],
        after=["Imi (意味): meaning"]),
])

POSTREAD = dict(title="Embeddings and Retrieval: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Embeddings", "Vectors that capture meaning; cosine similarity; distance = 1 - similarity; one model per index."],
        ["Vector database", "Indexes, metadata, filters, updates and scale. FAISS, Chroma, pgvector, Qdrant, Azure AI Search."],
        ["Flat, HNSW, IVF", "Flat is exact; HNSW (graph) and IVF (clusters) trade a little recall for big speed."],
        ["BM25", "Keyword relevance; great for codes, names and rare terms."],
        ["Hybrid + RRF", "Fuse ranked lists with sum of 1 / (k + rank)."],
        ["Re-ranking", "Score query-chunk pairs with a cross-encoder or LLM; keep the best few."],
        ["Measure", "hit@k and MRR on a test set; refusal accuracy on unanswerable questions."],
        ["Choosing an approach (NEW v4)", "RAG for large, changing facts; fine-tuning for style; long context for small corpora; caching for stable prefixes."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Query rewriting", paras=[
        "Ask the model to rewrite a vague or conversational question into a clear search query. \"And for Japan?\" "
        "becomes \"roaming charges in Japan\"."]),
    dict(sub="2. HyDE", paras=[
        "Hypothetical Document Embeddings: ask the model to draft an answer, embed the draft, and search with it. Drafts "
        "often look more like the target passages than short questions do."]),
    dict(sub="3. Cost-aware RAG", paras=[
        "Retrieval top-k drives input tokens. Retrieve wide, re-rank, and send only the best 3 to 5 chunks. Day 25 "
        "goes deeper on token optimisation."]),
    dict(sub="4. Re-indexing", paras=[
        "When you change embedding model or chunking, re-embed everything. Mixing vectors from different models in one "
        "index gives meaningless similarities."]),
    dict(sub="5. Combining approaches", paras=[
        "Real systems mix methods: a cached system prompt and tool list, RAG for facts, and sometimes a fine-tuned or "
        "small model for classification."]),
    dict(h="Part C: Check yourself", bullets=[
        "Why can two sentences with no shared words have similar embeddings?",
        "What does ANN give up in exchange for speed? How do HNSW and IVF differ?",
        "When does BM25 beat vector search?",
        "Why retrieve 20 candidates and re-rank to 3, instead of retrieving 3?",
        "A 600-page manual changes monthly and gets 10,000 questions a day. RAG, fine-tuning, long context or caching? Why?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Add metadata filtering by section to your retrieval function.",
        "Compute hit@3 and MRR for keyword, vector, hybrid and hybrid + re-rank on ten questions.",
        "Change the placeholder prices and query volume in the cost cell. When does caching win over RAG?"],
        after=["**Coming up on Day 23:** GenAI use cases by industry, maturity levels, and an SME session on security in the agentic world.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems on the handbook plus IT and travel FAQs. Offline embeddings are lexical stand-ins; "
                    "add a key for real semantic embeddings. Offline scores show how the code works, not real model quality.", problems=[
    dict(title="Similarity Matrix", level="Warm-up", concepts="embeddings, cosine similarity and distance",
         text="Embed 6 sentences (two about leave, two about travel, two about passwords) and print the cosine "
              "similarity and distance matrices. Which pairs are most similar?",
         sample="leave-1 vs leave-2: similarity 0.71 (online), distance 0.29\nleave-1 vs password-1: similarity 0.08",
         hints=["With unit vectors, similarity is vecs @ vecs.T."]),
    dict(title="Flat, HNSW and IVF", level="Medium", concepts="FAISS, recall, speed",
         text="On 20,000 random vectors, compare IndexFlatIP, IndexHNSWFlat and IndexIVFFlat: average query time and "
              "recall at 10. Try two values of efSearch and nprobe.",
         sample="Flat           0.30 ms/query  recall 1.00\nHNSW ef=64     0.17 ms/query  recall 0.70\nIVF nprobe=16  0.05 ms/query  recall 0.41\n(random vectors; real embeddings give higher recall)",
         hints=["Recall = overlap of top-10 sets / 10.", "IVF needs train() before add()."]),
    dict(title="BM25 for Codes", level="Easy", concepts="keyword search",
         text="Use BM25 to search for \"VPN-417\" and \"14 characters\". Compare the top result with vector search.",
         sample="BM25 top: c9 (VPN-417 ...)\nVector top (online): c9 or c10",
         hints=["Tokenise to lowercase words, keep codes like vpn-417 together."]),
    dict(title="Hybrid with RRF on Ten Questions", level="Medium", concepts="reciprocal rank fusion, hit@k, MRR",
         text="Fuse BM25 and vector rankings with RRF for ten test questions and compute hit@3 and MRR for BM25, "
              "vector and hybrid.",
         sample="method  hit@3  MRR      (example output; your numbers will differ)\nbm25    0.80   0.71\nvector  0.70   0.62\nhybrid  0.90   0.78",
         hints=["Write the expected chunk id for each question first."]),
    dict(title="Re-rank the Shortlist", level="Challenging", concepts="re-ranking",
         text="Retrieve the top 8 with hybrid search, re-rank with an LLM relevance score (online) or a word-overlap "
              "score (offline), and keep the top 3. Report hit@1 before and after re-ranking.",
         sample="hit@1 hybrid: 0.60 -> hybrid + re-rank: 0.80",
         hints=["Ask the model for a single integer 0 to 10 per candidate."]),
    dict(title="Choose the Approach", level="Medium", concepts="RAG, fine-tuning, long context, caching", new=True,
         text="For five scenarios (a 20-page policy asked 50 times a day; a 2,000-page manual updated weekly; a brand "
              "tone for replies; a 90,000 token contract reviewed clause by clause 5,000 times a day; a product catalogue that changes hourly), "
              "choose RAG, fine-tuning, long context, caching or a mix, and estimate monthly token cost with the "
              "placeholder prices in the notebook.",
         sample="20-page policy, 50/day      -> long context + cache (fits, few queries)\n"
                "2,000-page manual, weekly   -> RAG (too big, changes)\nbrand tone                  -> fine-tuning or examples",
         hints=["Facts that change: RAG. Style: fine-tuning or examples.", "Label every price as a placeholder."]),
    dict(title="Grounded Answers with a Threshold", level="Stretch", concepts="grounded generation, refusal",
         text="If the best re-ranked score is below a threshold, answer \"I don't know\" without calling the model. "
              "Tune the threshold on answerable and unanswerable questions and report both kinds of error.",
         sample="Threshold 0.25: 9/10 answerable answered, 2/2 unanswerable refused",
         hints=["Show false refusals and false answers separately."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "An embedding is a ________ that represents meaning.",
        "Cosine distance equals 1 minus cosine ________.",
        "A vector search that checks every vector is called ________ search.",
        "ANN stands for approximate nearest ________.",
        "HNSW is a ________-based ANN index; IVF is a cluster-based one.",
        "BM25 is a ________-based ranking method.",
        "RRF adds 1 / (k + ________) for each list.",
        "Reordering a shortlist with a more careful model is called ________.",
        "Teaching a model a style or format with examples and retraining is called ________.",
        "Reusing a large, stable prompt prefix at a lower price is prompt ________.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain embeddings using the map analogy.",
        "Compare flat, HNSW and IVF search, including what you trade.",
        "Describe a full retrieval pipeline from question to cited answer.",
        "When would you choose long context with caching instead of RAG? Use token cost in your answer.",
        "What did you learn from the Senior FDE interaction?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "import numpy as np\na = np.array([1.0, 0.0]); b = np.array([0.6, 0.8])\nprint(round(float(a @ b), 2), round(1 - float(a @ b), 2))",
        "def rrf(lists, k=60):\n    s = {}\n    for l in lists:\n        for r, d in enumerate(l, 1):\n"
        "            s[d] = s.get(d, 0) + 1 / (k + r)\n    return sorted(s, key=s.get, reverse=True)\n"
        "print(rrf([[\"a\", \"b\", \"c\"], [\"b\", \"c\", \"a\"]])[0])",
        "top_flat = {1, 2, 3, 4, 5}\ntop_ann = {1, 2, 3, 5, 9}\nprint(len(top_flat & top_ann) / 5)",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a function that returns the top-k chunk indices for a query vector."),
        dict(q="Write the RRF function."),
        dict(q="Write hit_at_k(search, tests, k) and mrr(search, tests)."),
        dict(q="Write monthly_cost(approach, ...) for long context, cached long context and RAG with placeholder prices."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

KNOWLEDGE = '''# Sakura Logistics Employee Handbook (sample)

## 1. Working hours
Standard working hours are 9:30 to 18:30, Monday to Friday. Teams in the Tokyo office follow JST and teams in the Bengaluru office follow IST.
Flexible start times between 8:00 and 11:00 are allowed with manager approval.

## 2. Leave policy
Full-time employees receive 18 days of paid leave per year. Leave accrues monthly at 1.5 days.
Unused leave can be carried forward up to a maximum of 10 days. Carried forward leave expires on 31 March of the following year.
Sick leave is separate: employees receive 8 days of paid sick leave per year. A medical certificate is required for sick leave longer than 2 consecutive days.

## 3. Remote work
Employees may work remotely up to 2 days per week. Remote work must be logged in the HR portal by 10:00 on the same day.
Remote work from another country requires approval from HR and the security team at least 14 days in advance.

## 4. Expenses
Travel expenses must be submitted within 30 days with receipts. Meals during business travel are reimbursed up to 2,000 INR or 4,000 JPY per day.
Expenses above 50,000 INR require approval from a director before booking.

## 5. Security
Laptops must use full disk encryption. Customer data must never be copied to personal devices or uploaded to unapproved AI tools.
Security incidents must be reported to security@sakura-logistics.example within 1 hour of discovery.

## IT FAQ
Error VPN-417 means your VPN certificate has expired. Renew it from the IT self-service portal and restart the VPN client.
Password resets are done through the self-service portal. Passwords must be at least 14 characters long.
Approved AI tools are listed on the IT intranet page. Do not paste customer data into tools that are not on that list.
New laptops are issued within 5 working days of a request approved by your manager.

## Travel FAQ
Book flights through the corporate travel desk at least 10 days before travel. Economy class is standard for flights under 6 hours.
Hotel stays are reimbursed up to 6,000 INR per night in India and 15,000 JPY per night in Japan.
Visa support letters are issued by HR within 3 working days.'''

NOTEBOOK = dict(subtitle="Embeddings, flat, HNSW and IVF indexes, hybrid search, re-ranking, and choosing RAG, fine-tuning, long context or caching", cells=[
    ("md", "## 1. Install"),
    ("code", '''# ===== Option A: Google Colab (active) =====
# Add your key once: click the key icon (Secrets) in the left sidebar, name it OPENAI_API_KEY, and allow notebook access.
!pip install -q openai tiktoken scikit-learn numpy pandas faiss-cpu rank_bm25

# ===== Option B: VS Code / local =====
# pip install openai tiktoken scikit-learn numpy pandas faiss-cpu rank_bm25
# Create a .env file (git-ignored) or set the variable in your terminal:  OPENAI_API_KEY=...
# No key? Everything still runs in OFFLINE demo mode with a tiny built-in stand-in model.
print("Setup done")'''),
    ("helpers",),
    ("md", "## 2. Documents and chunks"),
    ("code", "%%writefile knowledge.md\n" + KNOWLEDGE),
    ("code", '''import re, time, numpy as np, pandas as pd
text = open("knowledge.md").read()
chunks = []
for sec in re.split(r"\\n(?=## )", text):
    lines = sec.strip().splitlines()
    if not lines or not lines[0].startswith("## "):
        continue
    title = lines[0][3:].strip()
    for s in re.split(r"(?<=[.!?])\\s+", " ".join(lines[1:]).strip()):
        if s:
            chunks.append({"id": f"c{len(chunks) + 1}", "section": title, "text": s})
texts = [f"{c['section']}: {c['text']}" for c in chunks]
print(len(chunks), "chunks. Example:", chunks[0])'''),
    ("md", "## 3. Embeddings, cosine similarity and distance"),
    ("code", '''sents = ["How many leave days do I get?", "Employees receive 18 days of paid leave per year.",
         "What is the hotel limit in Tokyo?", "Hotel stays are reimbursed up to 15,000 JPY per night in Japan.",
         "How long must my password be?", "Passwords must be at least 14 characters long."]
V = embed(sents)
sim = pd.DataFrame(V @ V.T, index=[s[:22] for s in sents], columns=[f"s{i}" for i in range(6)]).round(2)
print("Cosine similarity\\n", sim)
print("\\nCosine distance (1 - similarity), first row:", (1 - sim.iloc[0]).round(2).tolist())
if not ONLINE:
    print("\\nOffline embeddings only match shared words. With a real model, questions match their answers by meaning.")'''),
    ("md", "## 4. A vector index with FAISS"),
    ("code", '''import faiss
vecs = embed(texts).astype("float32")
index = faiss.IndexFlatIP(vecs.shape[1])
index.add(vecs)

def vector_search(q, k=5):
    D, I = index.search(embed(q).astype("float32"), k)
    return [chunks[i]["id"] for i in I[0]]

for q in ["hotel limit in Japan", "VPN-417 error", "carry forward leave"]:
    print(f"{q:<22} -> {vector_search(q, 3)}")'''),
    ("md", "## 5. Exact vs approximate search at scale: flat, HNSW and IVF"),
    ("code", '''rng = np.random.default_rng(23)
X = rng.normal(size=(20000, 128)).astype("float32"); X /= np.linalg.norm(X, axis=1, keepdims=True)
Q = rng.normal(size=(200, 128)).astype("float32"); Q /= np.linalg.norm(Q, axis=1, keepdims=True)

def timed(idx):
    t = time.perf_counter(); _, I = idx.search(Q, 10)
    return I, (time.perf_counter() - t) / len(Q) * 1000

flat = faiss.IndexFlatIP(128); flat.add(X)
I_flat, t_flat = timed(flat)
recall = lambda I: np.mean([len(set(a) & set(b)) / 10 for a, b in zip(I_flat, I)])
rows = [{"index": "Flat (exact)", "ms/query": t_flat, "recall@10": 1.0}]

hnsw = faiss.IndexHNSWFlat(128, 32, faiss.METRIC_INNER_PRODUCT)
hnsw.hnsw.efConstruction = 80
hnsw.add(X)
for ef in [16, 64]:                        # efSearch: how widely HNSW explores per query
    hnsw.hnsw.efSearch = ef
    I, t = timed(hnsw); rows.append({"index": f"HNSW efSearch={ef}", "ms/query": t, "recall@10": recall(I)})

quant = faiss.IndexFlatIP(128)
ivf = faiss.IndexIVFFlat(quant, 128, 128, faiss.METRIC_INNER_PRODUCT)   # 128 clusters
ivf.train(X); ivf.add(X)
for nprobe in [4, 16]:                     # nprobe: how many clusters to search
    ivf.nprobe = nprobe
    I, t = timed(ivf); rows.append({"index": f"IVF nprobe={nprobe}", "ms/query": t, "recall@10": recall(I)})

print(pd.DataFrame(rows).round(3).to_string(index=False))
print("Random vectors are a hard case. Real embeddings cluster by topic, so ANN recall is usually higher at the same speed.")'''),
    ("md", "## 6. Metadata filters\nFilter by metadata **before** ranking. Permissions work the same way (Day 18)."),
    ("code", '''def filtered_search(q, k=3, section=None):
    pool = [i for i, c in enumerate(chunks) if section is None or c["section"] == section]
    sims = vecs[pool] @ embed(q)[0].astype("float32")
    return [chunks[pool[i]]["id"] for i in np.argsort(sims)[::-1][:k]]

print("All sections :", filtered_search("limit per night"))
print("Travel FAQ   :", filtered_search("limit per night", section="Travel FAQ"))'''),
    ("md", "## 7. Keyword search with BM25"),
    ("code", '''from rank_bm25 import BM25Okapi
tok = lambda s: re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", s.lower())
bm25 = BM25Okapi([tok(t) for t in texts])

def bm25_search(q, k=5):
    scores = bm25.get_scores(tok(q))
    return [chunks[i]["id"] for i in np.argsort(scores)[::-1][:k]]

for q in ["VPN-417", "14 characters", "visa letter"]:
    print(f"{q:<14} bm25 {bm25_search(q, 3)}   vector {vector_search(q, 3)}")'''),
    ("md", "## 8. Hybrid search with reciprocal rank fusion, measured on ten questions"),
    ("code", '''def rrf(rankings, k=60):
    scores = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking, 1):
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)

def hybrid_search(q, k=5):
    return rrf([bm25_search(q, 20), vector_search(q, 20)])[:k]

find = lambda frag: next(c["id"] for c in chunks if frag in c["text"])
tests = [("How many paid leave days do full-time staff get?", find("18 days of paid leave")),
         ("When does carried over leave expire?", find("expires on 31 March")),
         ("What does error VPN-417 mean?", find("VPN-417")),
         ("How long must a password be?", find("14 characters")),
         ("Hotel limit per night in Japan?", find("15,000 JPY")),
         ("How soon must I book flights?", find("10 days before travel")),
         ("Deadline to submit travel expenses?", find("within 30 days")),
         ("Who issues visa support letters?", find("Visa support letters")),
         ("How many sick days do employees get?", find("8 days of paid sick leave")),
         ("By when must remote work be logged?", find("logged in the HR portal"))]

def hit_rate(search, k=3):
    return np.mean([gold in search(q, k) for q, gold in tests])

def mrr(search, k=10):
    out = []
    for q, gold in tests:
        res = search(q, k)
        out.append(1 / (res.index(gold) + 1) if gold in res else 0)
    return np.mean(out)

table = pd.DataFrame({m: {"hit@3": hit_rate(f), "MRR": mrr(f)} for m, f in
                      {"bm25": bm25_search, "vector": vector_search, "hybrid": hybrid_search}.items()}).T.round(2)
print(table)'''),
    ("md", "## 9. Re-ranking"),
    ("code", '''by_id = {c["id"]: c for c in chunks}

def rerank(q, ids, keep=3):
    scored = []
    for cid in ids:
        c = by_id[cid]
        if ONLINE:
            r = llm(f"Rate 0 to 10 how well this passage answers the question. Reply with one integer.\\n"
                    f"Question: {q}\\nPassage: {c['text']}", temperature=0)
            nums = re.findall(r"\\d+", r)
            s = float(nums[0]) / 10 if nums else 0.0
        else:
            qw, cw = set(tok(q)), set(tok(c["section"] + " " + c["text"]))
            s = len(qw & cw) / max(1, len(qw))           # offline stand-in for a cross-encoder
        scored.append((cid, round(s, 2)))
    return sorted(scored, key=lambda x: x[1], reverse=True)[:keep]

reranked = lambda q, k=3: [cid for cid, _ in rerank(q, hybrid_search(q, 8), keep=k)]
table.loc["hybrid + re-rank"] = [hit_rate(reranked), mrr(reranked)]
print(table.round(2))
q = "When does carried over leave expire?"
print("\\nCandidates:", hybrid_search(q, 8))
print("Re-ranked: ", rerank(q, hybrid_search(q, 8)))'''),
    ("md", "## 10. Grounded answers with a refusal threshold"),
    ("code", '''RULES = "Answer using ONLY the context. Cite chunk ids like [c3]. If the context does not contain the answer, say \\"I don't know\\"."

def ask(q, threshold=0.3):
    top = rerank(q, hybrid_search(q, 8))
    if not top or top[0][1] < threshold:
        return "I don't know (no relevant passage found).", top
    context = "\\n".join(f"[{cid}] {by_id[cid]['text']}" for cid, _ in top)
    return llm(f"Context:\\n{context}\\n\\nQuestion: {q}", system=RULES, temperature=0), top

for q in ["What does error VPN-417 mean?", "Hotel limit per night in Japan?", "Can I bring my dog to the office?"]:
    a, top = ask(q)
    print(f"Q: {q}\\nA: {a}\\n   evidence: {top}\\n")'''),
    ("md", "### TODO 1: Add two more test questions (one unanswerable) and tune `threshold` so answerable questions are answered and the unanswerable one is refused."),
    ("code", "# TODO: write your code here"),
    ("md", "## 11. NEW (v4): RAG vs fine-tuning vs long context vs caching\nA rule-based helper plus a monthly token cost "
           "comparison. Prices are **placeholders**, not real prices. Real caching rules (minimum prefix length, cache "
           "lifetime, discount) vary by provider and model; check the documentation."),
    ("code", '''PRICE_PER_1M = {"input": 1.00, "cached_input": 0.10, "output": 4.00}   # PLACEHOLDER prices

def monthly_cost(corpus_tokens, queries_per_day, rag_context=1500, q_tokens=50, out_tokens=200, days=30):
    n = queries_per_day * days
    p = PRICE_PER_1M
    long_ctx = n * ((corpus_tokens + q_tokens) * p["input"] + out_tokens * p["output"]) / 1e6
    cached = n * (corpus_tokens * p["cached_input"] + q_tokens * p["input"] + out_tokens * p["output"]) / 1e6
    rag = n * ((rag_context + q_tokens) * p["input"] + out_tokens * p["output"]) / 1e6
    return {"long context": round(long_ctx, 2), "long context + cache": round(cached, 2), "RAG": round(rag, 2)}

def recommend(corpus_tokens, changes_per_month, queries_per_day, goal="facts", whole_doc=False, window=200_000):
    if goal == "style":
        return "fine-tuning or examples (style, not facts)"
    if corpus_tokens > window * 0.5:
        return "RAG (too big for the window)"
    if changes_per_month > 4:
        return "RAG (changes often: re-index, no retrain)"
    if whole_doc:
        return "long context + cache (needs the whole document)" if queries_per_day > 20 else "long context"
    cost = monthly_cost(corpus_tokens, queries_per_day)
    best = min(["long context + cache", "RAG"], key=cost.get)
    return f"{best} (cheapest)"

scenarios = [   # name, corpus tokens, changes per month, queries per day, goal, needs the whole document
    ("20-page policy, 50/day", 12_000, 1, 50, "facts", False),
    ("2,000-page manual, weekly updates", 1_200_000, 4, 3_000, "facts", False),
    ("brand tone for replies", 0, 0, 2_000, "style", False),
    ("90k token contract review, 5,000/day", 90_000, 0, 5_000, "facts", True),
    ("catalogue changing hourly", 300_000, 720, 8_000, "facts", False),
]
rows = []
for name, corpus, changes, qpd, goal, whole in scenarios:
    rec = recommend(corpus, changes, qpd, goal, whole)
    cost = monthly_cost(corpus, qpd) if goal == "facts" else {}
    rows.append({"scenario": name, "recommend": rec, **cost})
print(pd.DataFrame(rows).to_string(index=False))
print("\\nCosts are in placeholder units per month. Long context over a huge corpus may not fit the window at all.")'''),
    ("md", "### TODO 2 (SmartDesk step 19): run keyword, vector, hybrid and hybrid + re-rank on ten SmartDesk FAQ questions. "
           "Paste the hit-rate table for the hotel lab."),
    ("code", "# TODO: write your code here"),
    ("md", "## 12. Check yourself\n1. Which method won on codes like VPN-417, and why?\n2. Did re-ranking improve MRR?\n"
           "3. For which scenario does caching beat RAG on cost, and what would make you still choose RAG?"),
])

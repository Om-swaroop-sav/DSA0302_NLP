import math
import re
from collections import Counter

documents = {
    "D1": "python supports natural language processing",
    "D2": "natural language processing uses language models",
    "D3": "python programming supports data analysis",
}
query = "python language processing"

def terms(text): return re.findall(r"[a-z]+", text.lower())
N = len(documents)
doc_tokens = {name: terms(text) for name, text in documents.items()}
vocabulary = sorted(set(terms(query)).union(*(set(t) for t in doc_tokens.values())))
df = {term: sum(term in set(tokens) for tokens in doc_tokens.values()) for term in vocabulary}
idf = {term: math.log((N + 1) / (df[term] + 1)) + 1 for term in vocabulary}

def vector(tokens):
    counts = Counter(tokens); length = len(tokens) or 1
    return {term: (counts[term] / length) * idf[term] for term in vocabulary}

def cosine(a, b):
    dot = sum(a[t] * b[t] for t in vocabulary)
    na = math.sqrt(sum(v*v for v in a.values())); nb = math.sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0

qv = vector(terms(query))
scores = [(name, cosine(qv, vector(tokens))) for name, tokens in doc_tokens.items()]
print("Query:", query)
for name, score in sorted(scores, key=lambda item: item[1], reverse=True):
    print(f"{name}: {documents[name]} | TF-IDF cosine={score:.4f}")

"""Shared helpers for DSA03 NLP Assignment 2 task programs."""
import re
from pathlib import Path
from collections import Counter

SEED = 42
TOKEN_PATTERN = re.compile(r"\d{1,2}:\d{2}|[a-z]+(?:'[a-z]+)?|\d+")

def tokenize(text):
    return TOKEN_PATTERN.findall(text.lower())

def read_lines(filename, fallback=None):
    path = Path(filename)
    if path.exists():
        return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    print(f"[INFO] {filename} not found; using small demonstration data.")
    return list(fallback or [])

def split_80_10_10(items, seed=SEED):
    import random
    items = list(items)
    random.Random(seed).shuffle(items)
    n = len(items)
    a, b = int(.8*n), int(.9*n)
    return items[:a], items[a:b], items[b:]

def read_tagged(filename):
    """Read token<TAB>tag records; blank line separates sentences."""
    path = Path(filename)
    if not path.exists():
        return []
    result, current = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            if current:
                result.append(current)
                current = []
        else:
            parts = line.split()
            if len(parts) >= 2:
                current.append((parts[0], parts[-1]))
    if current:
        result.append(current)
    return result

def edit_distance(ref, hyp):
    previous = list(range(len(hyp) + 1))
    for i, r in enumerate(ref, 1):
        current = [i]
        for j, h in enumerate(hyp, 1):
            current.append(min(current[-1] + 1, previous[j] + 1,
                               previous[j-1] + (r != h)))
        previous = current
    return previous[-1]

def word_error_rate(reference, hypothesis):
    ref, hyp = tokenize(reference), tokenize(hypothesis)
    return edit_distance(ref, hyp) / len(ref) if ref else (0.0 if not hyp else 1.0)

import re

patterns = [
    ("DET", re.compile(r"^(the|a|an)$", re.I)),
    ("PRON", re.compile(r"^(i|you|he|she|it|we|they)$", re.I)),
    ("VERB", re.compile(r"^(is|am|are|was|were|run|runs|eat|eats|write|writes)$", re.I)),
    ("ADV", re.compile(r".*(ly)$", re.I)),
    ("ADJ", re.compile(r"^(quick|brown|small|intelligent|beautiful)$", re.I)),
    ("PUNCT", re.compile(r"^[.,!?]$")),
]
sentence = "The quick student writes carefully .".split()
for word in sentence:
    tag = next((label for label, pattern in patterns if pattern.fullmatch(word)), "NOUN")
    print(f"{word:15} {tag}")

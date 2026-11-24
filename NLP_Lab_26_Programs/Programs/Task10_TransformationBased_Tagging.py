words = "they book a book and students are playing".split()
# Initial lexical/default tagging.
lexicon = {"they": "PRP", "a": "DT", "and": "CC", "are": "VBP", "students": "NNS", "playing": "NN"}
tags = [lexicon.get(word.lower(), "NN") for word in words]
print("Initial:", list(zip(words, tags)))
# Transformation rules: -ing after an auxiliary becomes VBG; 'book' after a determiner stays noun.
for i, word in enumerate(words):
    if word.lower().endswith("ing") and i > 0 and tags[i - 1] in {"VBP", "VBZ", "VBD"}:
        tags[i] = "VBG"
    if word.lower() == "book" and i > 0 and tags[i - 1] == "PRP":
        tags[i] = "VBP"
print("After transformations:", list(zip(words, tags)))

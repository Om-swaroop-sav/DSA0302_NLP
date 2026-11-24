import re

text = (
    "Natural language processing studies human language. "
    "Language processing uses statistical and neural models. "
    "These models learn patterns from text data."
)
sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
stop = {"the", "a", "an", "is", "and", "from", "these", "uses"}
def content_words(sentence):
    return {w for w in re.findall(r"[a-z]+", sentence.lower()) if w not in stop}
sets = [content_words(s) for s in sentences]
print("Sentences:")
for i, s in enumerate(sentences, 1): print(f"{i}. {s}")
if len(sets) > 1:
    overlaps = []
    for i in range(len(sets)-1):
        union = sets[i] | sets[i+1]
        score = len(sets[i] & sets[i+1]) / len(union) if union else 0
        overlaps.append(score)
        print(f"Adjacent sentence {i}-{i+1} lexical overlap: {score:.3f}")
    coherence = sum(overlaps) / len(overlaps)
else:
    coherence = 1.0
print(f"Simple lexical-cohesion score: {coherence:.3f} (heuristic, not a validated language metric)")

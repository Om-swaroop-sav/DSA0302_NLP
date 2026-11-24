from collections import defaultdict, Counter
import random

corpus = "natural language processing helps computers understand human language natural language models learn patterns from text".split()
bigrams = defaultdict(Counter)
for first, second in zip(corpus, corpus[1:]):
    bigrams[first][second] += 1

rng = random.Random(7)
word = "natural"
generated = [word]
for _ in range(11):
    choices = list(bigrams.get(word, {"language": 1}).items())
    total = sum(count for _, count in choices)
    pick = rng.randrange(total)
    for candidate, count in choices:
        pick -= count
        if pick < 0:
            word = candidate
            break
    generated.append(word)
print("Training corpus:", " ".join(corpus))
print("Generated text:", " ".join(generated))
print("Bigram count:", sum(sum(row.values()) for row in bigrams.values()))

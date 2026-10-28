# Program: Bigram Model for Text Generation
import random

text = "i love india i love python i love programming"
words = text.split()
bigrams = {}

for i in range(len(words) - 1):
    bigrams.setdefault(words[i], []).append(words[i + 1])

for j in range(3):
    word = "i"
    result = [word]

    for i in range(6):
        if word not in bigrams:
            break
        word = random.choice(bigrams[word])
        result.append(word)

    print("Sentence", j + 1, ":", " ".join(result))

# Sample output (may vary because word selection is random):
# Sentence 1 : i love india i love python i
# Sentence 2 : i love programming
# Sentence 3 : i love python i love india i

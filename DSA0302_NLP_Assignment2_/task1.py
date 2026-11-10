"""Task 1: Counting words, vocabulary thresholds, OOV rate and Zipf plot."""
from collections import Counter
from common import tokenize, read_lines

DEMO = [
    "two tickets to vellore", "what is the bus fare to chennai",
    "book a ticket to madurai", "when is the next train",
    "i want to know the bus timing", "please cancel my ticket"
]

def simple_lemma(word):
    # Basic suffix heuristic for demonstration; manually validate linguistic lemmas.
    if len(word) > 4 and word.endswith("ies"): return word[:-3] + "y"
    if len(word) > 4 and word.endswith("ing"): return word[:-3]
    if len(word) > 3 and word.endswith("ed"): return word[:-2]
    if len(word) > 3 and word.endswith("s") and not word.endswith("ss"): return word[:-1]
    return word

def main():
    train = read_lines("train.txt", DEMO)
    dev = read_lines("dev.txt", DEMO[:2])
    tokens = [w for sentence in train for w in tokenize(sentence)]
    dev_tokens = [w for sentence in dev for w in tokenize(sentence)]
    counts = Counter(tokens)
    print("Utterances:", len(train))
    print("Tokens:", len(tokens))
    print("Types:", len(counts))
    print("Estimated lemmas:", len({simple_lemma(w) for w in tokens}))
    print("Top 10:", counts.most_common(10))

    for threshold in (1, 2, 3, 5):
        vocab = {w for w, c in counts.items() if c >= threshold}
        rare = sum(c for w, c in counts.items() if c < threshold)
        unk_percent = 100 * rare / len(tokens) if tokens else 0
        oov = sum(w not in vocab for w in dev_tokens)
        oov_percent = 100 * oov / len(dev_tokens) if dev_tokens else 0
        print(f"Threshold {threshold}: vocabulary={len(vocab)}, training UNK={rare} "
              f"({unk_percent:.2f}%), dev OOV={oov} ({oov_percent:.2f}%)")

    try:
        import matplotlib.pyplot as plt
        frequencies = sorted(counts.values(), reverse=True)
        plt.figure()
        plt.loglog(range(1, len(frequencies)+1), frequencies, marker=".")
        plt.xlabel("Word rank"); plt.ylabel("Frequency")
        plt.title("Zipf's Law")
        plt.tight_layout(); plt.savefig("task1_zipf.png"); plt.close()
        print("Saved task1_zipf.png")
    except ImportError:
        print("Install matplotlib to create the Zipf plot.")

if __name__ == "__main__":
    main()

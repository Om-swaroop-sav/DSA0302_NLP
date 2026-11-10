"""Task 5: Cross-entropy, perplexity and word error rate."""
import math
from collections import Counter
from common import tokenize, read_lines, word_error_rate

DEMO_TRAIN = ["two tickets to vellore", "book a ticket to madurai",
              "what is the bus fare to chennai"]
DEMO_TEST = ["two tickets to chennai", "when is the next train"]

def evaluate_unigram(train, test, k=0.1):
    counts = Counter(w for s in train for w in tokenize(s))
    vocab = set(counts) | {"<UNK>"}
    total = sum(counts.values())
    log_probability, n = 0.0, 0
    for sentence in test:
        for word in tokenize(sentence):
            p = (counts[word] + k) / (total + k*len(vocab))
            log_probability += math.log2(p)
            n += 1
    cross_entropy = -log_probability/n if n else float("inf")
    perplexity = 2**cross_entropy if n else float("inf")
    return cross_entropy, perplexity

def main():
    train = read_lines("train.txt", DEMO_TRAIN)
    test = read_lines("test.txt", DEMO_TEST)
    h, pp = evaluate_unigram(train, test)
    print(f"Unigram cross-entropy: {h:.4f} bits")
    print(f"Unigram perplexity: {pp:.4f}")
    ref = "two tickets to vellore"
    hyp = "to tickets to vellore"
    print(f"Example WER: {word_error_rate(ref,hyp)*100:.2f}%")
    print("For assignment comparisons, calculate all models using the same held-out test set.")

if __name__ == "__main__":
    main()

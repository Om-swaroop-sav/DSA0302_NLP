"""Task 3: Add-one, Add-k and Good-Turing smoothing demonstrations."""
from collections import Counter
from common import tokenize, read_lines

DEMO = ["two tickets to vellore", "two tickets to chennai",
        "book a ticket to madurai", "book a bus ticket"]

def main():
    corpus = read_lines("train.txt", DEMO)
    unigram, bigram, context = Counter(), Counter(), Counter()
    for sentence in corpus:
        words = ["<s>"] + tokenize(sentence) + ["</s>"]
        for a, b in zip(words, words[1:]):
            unigram[b] += 1
            bigram[(a, b)] += 1
            context[a] += 1
    vocabulary_size = len(unigram) + 1
    total = sum(unigram.values())

    previous, word = "to", "vellore"
    count = bigram[(previous, word)]
    denominator = context[previous]
    for k in (1, 0.5, 0.1):
        probability = (count + k) / (denominator + k*vocabulary_size)
        print(f"Add-k k={k}: P({word}|{previous})={probability:.6f}")

    # Good-Turing adjusted count: r* = (r+1) N_(r+1) / N_r
    frequency_of_frequency = Counter(bigram.values())
    r = count
    nr, nr1 = frequency_of_frequency[r], frequency_of_frequency[r+1]
    adjusted = (r+1)*nr1/nr if nr and nr1 else float(r)
    print("Observed bigram count:", r)
    print("Good-Turing adjusted count (fallback to raw count if unavailable):", adjusted)
    print("Note: full Good-Turing requires estimating unseen n-gram probability mass.")

if __name__ == "__main__":
    main()

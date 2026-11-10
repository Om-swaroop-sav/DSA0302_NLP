"""Task 2: Unsmoothed unigram, bigram and trigram language models."""
from collections import Counter
from common import tokenize, read_lines

DEMO = ["two tickets to vellore", "book a ticket to madurai",
        "what is the bus fare to chennai", "when is the next train"]

class NgramModel:
    def __init__(self, sentences):
        self.uni, self.bi, self.tri = Counter(), Counter(), Counter()
        self.ctx1, self.ctx2 = Counter(), Counter()
        for sentence in sentences:
            words = ["<s>", "<s>"] + tokenize(sentence) + ["</s>"]
            for i in range(2, len(words)):
                self.uni[words[i]] += 1
                self.bi[(words[i-1], words[i])] += 1
                self.tri[(words[i-2], words[i-1], words[i])] += 1
                self.ctx1[words[i-1]] += 1
                self.ctx2[(words[i-2], words[i-1])] += 1
        self.total = sum(self.uni.values())

    def unigram(self, word):
        return self.uni[word] / self.total if self.total else 0

    def bigram(self, previous, word):
        return self.bi[(previous, word)] / self.ctx1[previous] if self.ctx1[previous] else 0

    def trigram(self, first, second, word):
        context = (first, second)
        return self.tri[(first, second, word)] / self.ctx2[context] if self.ctx2[context] else 0

    def sentence_probability(self, sentence, order=2):
        seq = ["<s>", "<s>"] + tokenize(sentence) + ["</s>"]
        probability = 1.0
        for i in range(2, len(seq)):
            if order == 1: p = self.unigram(seq[i])
            elif order == 2: p = self.bigram(seq[i-1], seq[i])
            else: p = self.trigram(seq[i-2], seq[i-1], seq[i])
            probability *= p
        return probability

def main():
    corpus = read_lines("train.txt", DEMO)
    model = NgramModel(corpus)
    sentence = "two tickets to vellore"
    for n in (1, 2, 3):
        print(f"{n}-gram probability of '{sentence}':",
              model.sentence_probability(sentence, n))
    print("P(ticket):", model.unigram("ticket"))
    print("P(ticket|a):", model.bigram("a", "ticket"))
    print("P(ticket|book,a):", model.trigram("book", "a", "ticket"))

if __name__ == "__main__":
    main()

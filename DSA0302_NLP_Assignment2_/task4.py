"""Task 4: Backoff and deleted-interpolation style language-model scoring."""
from collections import Counter
from common import tokenize, read_lines

DEMO = ["two tickets to vellore", "two tickets to chennai",
        "book a ticket to madurai", "what is the bus fare"]

class BackoffModel:
    def __init__(self, corpus):
        self.uni, self.bi, self.tri = Counter(), Counter(), Counter()
        self.c1, self.c2 = Counter(), Counter()
        for sentence in corpus:
            words = ["<s>", "<s>"] + tokenize(sentence) + ["</s>"]
            for i in range(2, len(words)):
                self.uni[words[i]] += 1
                self.bi[(words[i-1], words[i])] += 1
                self.tri[(words[i-2], words[i-1], words[i])] += 1
                self.c1[words[i-1]] += 1
                self.c2[(words[i-2], words[i-1])] += 1
        self.total = sum(self.uni.values())

    def p1(self, w):
        return self.uni[w]/self.total if self.total else 0

    def p2(self, a, w):
        return self.bi[(a,w)]/self.c1[a] if self.c1[a] else 0

    def p3(self, a, b, w):
        return self.tri[(a,b,w)]/self.c2[(a,b)] if self.c2[(a,b)] else 0

    def stupid_backoff(self, a, b, w, alpha=.4):
        if self.p3(a,b,w): return self.p3(a,b,w)
        if self.p2(b,w): return alpha*self.p2(b,w)
        return alpha**2*self.p1(w)

    def katz_style_backoff(self, a, b, w, alpha=.4):
        # Simplified educational backoff score; not full Katz alpha estimation.
        if self.p3(a,b,w): return self.p3(a,b,w)
        if self.p2(b,w): return alpha*self.p2(b,w)
        return alpha**2*max(self.p1(w), 1e-12)

    def interpolation(self, a, b, w, lambdas=(.2,.3,.5)):
        l1,l2,l3 = lambdas
        return l1*self.p1(w) + l2*self.p2(b,w) + l3*self.p3(a,b,w)

def main():
    model = BackoffModel(read_lines("train.txt", DEMO))
    context = ("two", "tickets", "vellore")
    print("Stupid Backoff:", model.stupid_backoff(*context))
    print("Katz-style simplified backoff:", model.katz_style_backoff(*context))
    print("Interpolated score:", model.interpolation(*context))
    print("Interpolation weights:", (0.2, 0.3, 0.5),
          "(choose/tune on development data; these are examples)")

if __name__ == "__main__":
    main()

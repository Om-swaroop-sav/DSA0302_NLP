"""Task 9: PCFG rule probabilities and Viterbi CKY parsing.
Run: python task9_pcfg.py
The example grammar is in Chomsky Normal Form (CNF).
"""
import math

# Each rule is (LHS, RHS, probability).
RULES = [
    ("S", ("NP", "VP"), 1.0),
    ("NP", ("DET", "N"), 0.7),
    ("NP", ("PRON",), 0.3),   # unary lexical-category shortcut
    ("VP", ("V", "NP"), 0.8),
    ("VP", ("V",), 0.2),
    ("DET", ("the",), 0.8),
    ("DET", ("a",), 0.2),
    ("N", ("student",), 0.4),
    ("N", ("timetable",), 0.3),
    ("N", ("form",), 0.3),
    ("PRON", ("i",), 0.5),
    ("PRON", ("you",), 0.5),
    ("V", ("checks",), 0.5),
    ("V", ("submits",), 0.3),
    ("V", ("books",), 0.2),
]

def validate_probabilities(rules):
    totals = {}
    for lhs, rhs, probability in rules:
        totals[lhs] = totals.get(lhs, 0.0) + probability
    print("Probability totals by LHS:")
    for lhs, total in sorted(totals.items()):
        print(f"  {lhs}: {total:.3f}")

def viterbi(words):
    n = len(words)
    chart = {}
    back = {}
    # lexical rules
    for i, word in enumerate(words):
        for lhs, rhs, prob in RULES:
            if len(rhs) == 1 and rhs[0] == word:
                chart[(i, i + 1, lhs)] = math.log(prob)
                back[(i, i + 1, lhs)] = ("LEX", word)

    # unary rules such as NP -> PRON
    for i in range(n):
        changed = True
        while changed:
            changed = False
            for lhs, rhs, prob in RULES:
                if len(rhs) == 1 and rhs[0].isupper():
                    child = (i, i + 1, rhs[0])
                    parent = (i, i + 1, lhs)
                    if child in chart:
                        score = math.log(prob) + chart[child]
                        if score > chart.get(parent, -math.inf):
                            chart[parent] = score
                            back[parent] = ("UNARY", child)
                            changed = True

    # binary rules
    for span in range(2, n + 1):
        for i in range(n - span + 1):
            j = i + span
            for k in range(i + 1, j):
                for lhs, rhs, prob in RULES:
                    if len(rhs) == 2:
                        left = (i, k, rhs[0])
                        right = (k, j, rhs[1])
                        parent = (i, j, lhs)
                        if left in chart and right in chart:
                            score = math.log(prob) + chart[left] + chart[right]
                            if score > chart.get(parent, -math.inf):
                                chart[parent] = score
                                back[parent] = ("BINARY", left, right)

    root = (0, n, "S")
    if root not in chart:
        return None, None
    def build(node):
        kind, *children = back[node]
        if kind == "LEX":
            return children[0]
        if kind == "UNARY":
            return (node[2], build(children[0]))
        return (node[2], build(children[0]), build(children[1]))
    return build(root), math.exp(chart[root])

def main():
    validate_probabilities(RULES)
    sentence = input("\nEnter sentence (example: the student checks the timetable): ")
    words = sentence.lower().split()
    tree, probability = viterbi(words)
    if tree is None:
        print("No parse found. This small PCFG supports only its listed words/rules.")
    else:
        print("Best parse:", tree)
        print(f"Viterbi tree probability: {probability:.8f}")

if __name__ == "__main__":
    main()

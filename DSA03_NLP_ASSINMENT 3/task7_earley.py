"""Task 7: General Earley chart parser (Predictor, Scanner, Completer).
Run: python task7_earley.py
"""
import re
from collections import defaultdict

GRAMMAR = {
    "S": [["NP", "VP"], ["AUX", "NP", "VP"], ["WH", "AUX", "NP", "VP"], ["VP"]],
    "NP": [["DET", "N"], ["PRON"], ["NAME"]],
    "VP": [["V"], ["V", "NP"], ["V", "PP"], ["V", "NP", "PP"]],
    "PP": [["PREP", "NP"]],
}
LEXICON = {
    "DET": {"the", "a", "an", "this", "that"},
    "N": {"student", "form", "timetable", "room", "library", "exam",
          "notice", "fee", "receipt", "hostel", "ticket"},
    "PRON": {"i", "you", "we", "they", "he", "she"},
    "NAME": {"om", "ajay"},
    "V": {"checks", "check", "submits", "submit", "books", "book",
          "starts", "start", "pays", "pay", "shows", "show"},
    "AUX": {"can", "could", "does", "do", "will"},
    "WH": {"when", "where", "what", "which", "who", "how"},
    "PREP": {"in", "on", "at", "near", "with", "for", "to", "from"},
}
NONTERMINALS = set(GRAMMAR)

def tokenize(text):
    return re.findall(r"[A-Za-z]+|[0-9]+", text.lower())

def earley_parse(words):
    n = len(words)
    chart = [set() for _ in range(n + 1)]
    # State format: (lhs, rhs tuple, dot position, origin)
    chart[0].add(("ROOT", ("S",), 0, 0))

    for i in range(n + 1):
        changed = True
        while changed:
            changed = False
            for state in list(chart[i]):
                lhs, rhs, dot, origin = state

                # COMPLETER
                if dot == len(rhs):
                    for prev in list(chart[origin]):
                        plhs, prhs, pdot, porigin = prev
                        if pdot < len(prhs) and prhs[pdot] == lhs:
                            new_state = (plhs, prhs, pdot + 1, porigin)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

                elif rhs[dot] in NONTERMINALS:
                    # PREDICTOR
                    symbol = rhs[dot]
                    for production in GRAMMAR[symbol]:
                        new_state = (symbol, tuple(production), 0, i)
                        if new_state not in chart[i]:
                            chart[i].add(new_state)
                            changed = True
                else:
                    # SCANNER
                    symbol = rhs[dot]
                    if i < n and words[i] in LEXICON.get(symbol, set()):
                        chart[i + 1].add((lhs, rhs, dot + 1, origin))

    accepted = ("ROOT", ("S",), 1, 0) in chart[n]
    return accepted, chart

def display_chart(chart):
    for i, states in enumerate(chart):
        print(f"\nCHART[{i}]")
        for lhs, rhs, dot, origin in sorted(states):
            before = " ".join(rhs[:dot])
            after = " ".join(rhs[dot:])
            print(f"  {lhs} -> {before} • {after}  [{origin}]")

if __name__ == "__main__":
    sentence = input("Enter a helpdesk sentence: ").strip()
    words = tokenize(sentence)
    accepted, chart = earley_parse(words)
    print("\nPredictor: adds productions for expected non-terminals.")
    print("Scanner: matches the next input token.")
    print("Completer: advances states waiting for a completed phrase.")
    display_chart(chart)
    print("\nResult:", "ACCEPTED" if accepted else "REJECTED")
    print("Total chart states:", sum(len(x) for x in chart))

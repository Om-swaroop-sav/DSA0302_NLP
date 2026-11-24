try:
    from nltk import CFG, ChartParser
    grammar = CFG.fromstring("""
        S -> NP VP
        NP -> Det Adj N
        VP -> V NP
        Det -> 'the'
        Adj -> 'young'
        N -> 'student' | 'book'
        V -> 'reads'
    """)
    sentence = "the young student reads the book".split()
    trees = list(ChartParser(grammar).parse(sentence))
    print("Sentence:", " ".join(sentence))
    for tree in trees:
        print(tree)
        tree.pretty_print()
except ImportError:
    print("SKIPPED: NLTK is not installed. Run setup_core.ps1.")

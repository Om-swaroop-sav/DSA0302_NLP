try:
    from nltk import CFG, EarleyChartParser
    grammar = CFG.fromstring("""
        S -> NP VP
        NP -> Det N | 'John'
        VP -> V NP | V
        Det -> 'the' | 'a'
        N -> 'dog' | 'cat'
        V -> 'saw' | 'slept'
    """)
    sentence = "John saw the dog".split()
    trees = list(EarleyChartParser(grammar).parse(sentence))
    print("Sentence:", " ".join(sentence))
    print("Earley parse count:", len(trees))
    for tree in trees:
        print(tree)
except ImportError:
    print("SKIPPED: NLTK is not installed. Run setup_core.ps1.")

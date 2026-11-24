try:
    from nltk import CFG, RecursiveDescentParser
    grammar = CFG.fromstring("""
        S -> NP VP
        NP -> Det N
        VP -> V NP
        Det -> 'the' | 'a'
        N -> 'student' | 'book'
        V -> 'reads' | 'likes'
    """)
    sentence = "the student reads a book".split()
    trees = list(RecursiveDescentParser(grammar).parse(sentence))
    print("Sentence:", " ".join(sentence))
    print("Parse count:", len(trees))
    for tree in trees:
        print(tree)
except ImportError:
    print("SKIPPED: NLTK is not installed. Run setup_core.ps1.")

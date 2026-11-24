try:
    from nltk import PCFG
    from nltk.parse import ViterbiParser
    grammar = PCFG.fromstring("""
        S -> NP VP [1.0]
        NP -> Det N [0.6] | Name [0.4]
        VP -> V NP [0.7] | V [0.3]
        Det -> 'the' [1.0]
        N -> 'dog' [0.5] | 'cat' [0.5]
        Name -> 'John' [1.0]
        V -> 'saw' [0.6] | 'slept' [0.4]
    """)
    sentence = "John saw the dog".split()
    parses = list(ViterbiParser(grammar).parse(sentence))
    print("Sentence:", " ".join(sentence))
    if parses:
        for tree in parses:
            print(tree)
            print("Probability:", tree.prob())
    else:
        print("No parse found")
except ImportError:
    print("SKIPPED: NLTK is not installed. Run setup_core.ps1.")

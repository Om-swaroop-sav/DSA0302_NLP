try:
    from nltk import CFG, ChartParser
    grammar = CFG.fromstring("""
        S -> NP_S VP_S | NP_P VP_P
        NP_S -> 'the' 'student'
        NP_P -> 'the' 'students'
        VP_S -> 'writes' 'code'
        VP_P -> 'write' 'code'
    """)
    parser = ChartParser(grammar)
    for sentence in ["the student writes code", "the students write code", "the student write code", "the students writes code"]:
        accepted = any(parser.parse(sentence.split()))
        print(f"{sentence:30} -> {'AGREEMENT OK' if accepted else 'AGREEMENT ERROR'}")
except ImportError:
    print("SKIPPED: NLTK is not installed. Run setup_core.ps1.")

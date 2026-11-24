try:
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
    words = ["playing", "played", "player", "studies", "studying", "connected", "connection", "generously"]
    for word in words:
        print(f"{word:15} -> {stemmer.stem(word)}")
except ImportError:
    print("SKIPPED: NLTK is not installed. Run setup_core.ps1.")

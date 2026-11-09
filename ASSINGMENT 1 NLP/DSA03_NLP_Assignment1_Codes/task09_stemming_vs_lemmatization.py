try:
    import nltk
    from nltk.stem import PorterStemmer, WordNetLemmatizer
except ImportError:
    raise SystemExit("NLTK is required. Install it using: python -m pip install nltk")

# WordNet data is needed for lemmatisation.
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

samples = [
    ("fractures", "n"),
    ("studies", "n"),
    ("patients", "n"),
    ("infections", "n"),
    ("treated", "v"),
]

if __name__ == "__main__":
    for word, pos in samples:
        print(f"Word: {word}")
        print(f"Porter stem: {stemmer.stem(word)}")
        print(f"Lemma: {lemmatizer.lemmatize(word, pos=pos)}")
        print()

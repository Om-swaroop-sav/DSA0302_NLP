try:
    from nltk.stem import PorterStemmer
except ImportError:
    raise SystemExit("NLTK is required. Install it using: python -m pip install nltk")

stemmer = PorterStemmer()

words = [
    "fractures", "fractured", "fracturing", "infections",
    "patients", "operating", "connected", "studies"
]

if __name__ == "__main__":
    for word in words:
        print(f"{word} -> {stemmer.stem(word)}")

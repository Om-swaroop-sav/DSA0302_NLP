import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["playing", "played", "players", "studies", "running"]
for word in words:
    stem = stemmer.stem(word)
    print("Word:", word)
    print("Stem:", stem)
    print()

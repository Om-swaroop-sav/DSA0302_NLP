# 5. Porter Stemmer Algorithm
# Install: pip install nltk

from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ["playing", "played", "plays", "studies", "studying", "running"]

print("Original Word -> Stemmed Word")
for word in words:
    print(word, "->", ps.stem(word))

# Sample output:
# Original Word -> Stemmed Word
# playing -> play
# played -> play
# plays -> play
# studies -> studi
# studying -> studi
# running -> run

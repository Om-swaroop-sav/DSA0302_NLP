# Program: Stemming and Lemmatization
# Install: pip install nltk

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")

ps = PorterStemmer()
lem = WordNetLemmatizer()

words = ["playing", "played", "studies", "running"]
sentence = "The boys are playing cricket"

print("Word\tStem\tLemma")
for word in words:
    print(word, "\t", ps.stem(word), "\t", lem.lemmatize(word))

print("\nSentence Word Analysis:")
for word in word_tokenize(sentence):
    lower = word.lower()
    # Supply a verb POS for common verb forms so their lemmas are correct.
    verb_words = {"are", "playing", "played", "running"}
    pos = "v" if lower in verb_words else "n"
    print(word, "-> Stem:", ps.stem(lower),
          "| Lemma:", lem.lemmatize(lower, pos))

# Sample output:
# Word    Stem      Lemma
# playing play      playing
# played  play      played
# studies studi     study
# running run       running
#
# Sentence Word Analysis:
# The -> Stem: the | Lemma: the
# boys -> Stem: boy | Lemma: boy
# are -> Stem: ar | Lemma: be
# playing -> Stem: play | Lemma: play
# cricket -> Stem: cricket | Lemma: cricket

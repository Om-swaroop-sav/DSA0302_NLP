# Program: Morphological Analysis Using NLTK
# Install: pip install nltk

import nltk
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("wordnet")

sentence = "The boys are playing cricket"
words = word_tokenize(sentence)
tags = pos_tag(words)
lem = WordNetLemmatizer()

print("Word -> Root | POS")
for word, tag in tags:
    if tag.startswith("V"):
        pos = "v"
    elif tag.startswith("J"):
        pos = "a"
    elif tag.startswith("R"):
        pos = "r"
    else:
        pos = "n"
    root = lem.lemmatize(word.lower(), pos)
    print(f"{word} -> Root: {root} | POS: {tag}")

# Sample output (POS tags can vary slightly by NLTK version):
# Word -> Root | POS
# The -> Root: the | POS: DT
# boys -> Root: boy | POS: NNS
# are -> Root: be | POS: VBP
# playing -> Root: play | POS: VBG
# cricket -> Root: cricket | POS: NN

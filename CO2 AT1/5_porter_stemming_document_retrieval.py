# 5. Porter Stemmer-Based Preprocessing for Document Retrieval
# Install: pip install nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["relational", "relation", "relate"]
print(f"{'Original word':<16}{'Porter stem':<16}{'Explanation'}")
print("-" * 65)
for word in words:
    stem = stemmer.stem(word)
    if word == "relational":
        explanation = "Porter suffix rules reduce -ational"
    elif word == "relation":
        explanation = "Porter suffix rules reduce -ation"
    else:
        explanation = "Porter stemmer removes final e"
    print(f"{word:<16}{stem:<16}{explanation}")


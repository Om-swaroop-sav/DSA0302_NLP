# 6. N-gram Model: Unigrams, Bigrams, Trigrams and Next-Word Prediction
# Install: pip install nltk

from nltk import word_tokenize, ngrams
from collections import Counter

sentence = "I love India and I love Python"
words = word_tokenize(sentence)

print("Unigrams:", list(ngrams(words, 1)))
print("Bigrams:", list(ngrams(words, 2)))
print("Trigrams:", list(ngrams(words, 3)))

corpus = "i love india i love python i love programming"
tokens = corpus.split()
bigram_counts = Counter(zip(tokens, tokens[1:]))

word = input("\nEnter a word: ").lower()
next_words = {
    next_word: count
    for (current_word, next_word), count in bigram_counts.items()
    if current_word == word
}

if next_words:
    highest_count = max(next_words.values())
    prediction = next(
        next_word for next_word, count in next_words.items()
        if count == highest_count
    )
    print("Next word:", prediction)
else:
    print("No next word found")

# Sample output (input: love):
# Unigrams: [('I',), ('love',), ('India',), ('and',), ('I',), ('love',), ('Python',)]
# Bigrams: [('I', 'love'), ('love', 'India'), ('India', 'and'), ('and', 'I'), ('I', 'love'), ('love', 'Python')]
# Trigrams: [('I', 'love', 'India'), ('love', 'India', 'and'), ('India', 'and', 'I'), ('and', 'I', 'love'), ('I', 'love', 'Python')]
#
# Enter a word: love
# Next word: india

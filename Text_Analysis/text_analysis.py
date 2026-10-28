import re
from collections import Counter
text = "Python is easy. Python is powerful. Python is useful."
words = re.findall(r'\b\w+\b', text.lower())
sentences = re.split(r'[.!?]', text)
print("Words:", words)
print("Sentences:", [s.strip() for s in sentences if s.strip()])
print("Word count:", len(words))
most = Counter(words).most_common(1)
print("Most frequent word:", most[0][0])

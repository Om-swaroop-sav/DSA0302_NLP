# 2. Morphological Parsing for Sentiment Analysis
words = ["unhappy", "happiness", "happily"]
data = {
    "unhappy": ("un-", "happy", "-", "Derivational", "happy"),
    "happiness": ("-", "happy", "-ness", "Derivational", "happy"),
    "happily": ("-", "happi", "-ly", "Derivational", "happy"),
}
print(f"{'Word':<14}{'Prefix':<10}{'Base':<10}{'Suffix':<10}{'Type':<16}{'Normalized root'}")
print("-" * 80)
for word in words:
    prefix, base, suffix, kind, normalized = data[word]
    print(f"{word:<14}{prefix:<10}{base:<10}{suffix:<10}{kind:<16}{normalized}")

